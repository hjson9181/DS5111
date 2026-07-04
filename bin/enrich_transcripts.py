#!/usr/bin/env python3
import sys
import os
import json
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types
from abc import ABC, abstractmethod

# Load environmental configurations from local workspace files
load_dotenv()

# Audit logging framework tracking pipeline telemetry
logging.basicConfig(
    filename='pipeline_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Enrichment contract (interfact)
class LLMStrategy(ABC):
    @abstractmethod
    def enrich(self, video_id: str, raw_text: str) -> dict:
        """
        Must accept a video identifier and raw transcript text, and return
        a schema-compliant dictionary containing at minimum:
            - video_id: str
            - cleaned_text: str
            - tech_terms: list[str]
            - book_names: list[str]
        """
        pass
# =====================================================================
# 2. STRATEGY A: THE PRODUCTION GEMINI ENRICHER
# =====================================================================
class GeminiStrategy(LLMStrategy):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            logging.critical("GEMINI_API_KEY missing — cannot initialize GeminiStrategy.")
            raise ValueError("GEMINI_API_KEY is required to initialize GeminiStrategy.")

        self.client = genai.Client(api_key=self.api_key)

        self.response_schema = {
            "type": "OBJECT",
            "properties": {
                "video_id": {"type": "STRING"},
                "cleaned_text": {"type": "STRING"},
                "tech_terms": {"type": "ARRAY", "items": {"type": "STRING"}},
                "book_names": {"type": "ARRAY", "items": {"type": "STRING"}},
            },
            "required": ["video_id", "cleaned_text"],
        }

    def enrich(self, video_id: str, raw_text: str) -> dict:
        prompt = f"""
        You are an elite data engineer. Clean this transcript text for video_id '{video_id}'.
        1. Strip all timestamps and duration codes.
        2. Extract technical architecture terms and books.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{prompt}\n\nTRANSCRIPT:\n{raw_text}",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=self.response_schema,
            ),
        )

        return json.loads(response.text)
        
# TODO: implement in next step — prompt construction + generate_content call
        #raise NotImplementedError
    
def main():
    logging.info("Pipeline Step 2B (Gemini Enrichment) started.")
    
    # -------------------------------------------------------------------------
    # TODO 1: API Environment Validation and Client Initialization
    # Extract the necessary credential key token from the local environment.
    # If the token is missing, log a critical failure and terminate the system.
    # Otherwise, instantiate the official Google GenAI Client utility.
    # -------------------------------------------------------------------------
    # === YOUR CODE HERE ===
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        logging.critical("GEMINI_API_KEY")
        sys.exit(1)
    client = genai.Client(api_key = GEMINI_API_KEY)
    # ======================

    # -------------------------------------------------------------------------
    # TODO 2: Structured Output Response Schema Definition
    # To prevent the LLM from returning unpredictable formats that would crash
    # downstream applications, define a strict "Data Contract" using a JSON 
    # Schema layout. 
    # 
    # Enforce a response type of "OBJECT" that guarantees the presence of:
    #   - video_id: (STRING, Required)
    #   - cleaned_text: (STRING, Required)
    #   - tech_terms: (ARRAY of STRINGS)
    #   - book_names: (ARRAY of STRINGS)
    # -------------------------------------------------------------------------
    response_schema = {
        "type": "OBJECT",
        "properties": {
            "video_id": {"type": "STRING"},
            "cleaned_text": {"type": "STRING"},
            "tech_terms": {"type": "ARRAY", "items": {"type": "STRING"}},
            "book_names": {"type": "ARRAY", "items": {"type": "STRING"}},  
        },
        "required": ["video_id", "cleaned_text"],
    }

    # Stream processing framework reading line-by-line text inputs from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        # ---------------------------------------------------------------------
        # TODO 3: Inbound String Stream Deserialization
        # Safely wrap your stream ingestion inside an isolated try-except block.
        # Parse the raw line string object into a key-value dictionary and 
        # extract the target 'video_id' and 'raw_text' properties. 
        # Log any malformed line tracks and continue processing the stream.
        # ---------------------------------------------------------------------
        try:
            # EXTRACT PAYLOAD DETAILS HERE
            data = json.loads(line)
            video_id = data["video_id"]
            raw_text = data["raw_text"]
        except Exception as e:
            logging.error(f"Failed to parse incoming JSON payload row: {str(e)}")
            continue

        logging.info(f"Orchestrating Gemini enrichment for video: {video_id}")
        
        prompt = f"""
        You are an elite data engineer. Clean this transcript text for video_id '{video_id}'.
        1. Strip all timestamps and duration codes.
        2. Extract technical architecture terms and books.
        """

        # ---------------------------------------------------------------------
        # TODO 4: Structured Model Invocation and Instant Stream Flushing
        # Call the 'gemini-2.5-flash' model via the unified SDK interface.
        # Inject the constructed prompt along with the raw text sequence payload.
        # Map the configuration block to use the structured JSON mime-type 
        # and enforce your defined response schema parameters.
        # Write the resulting text explicitly to sys.stdout and flush immediately.
        # ---------------------------------------------------------------------
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{prompt}\n\nTRANSCRIPT:\n{raw_text}",
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=response_schema,
                ),
            )
            # INVOCATION AND EMISSION PATTERN HERE
            sys.stdout.write(response.text + "\n")
            sys.stdout.flush()
            
        except Exception as e:
            logging.error(f"Failed processing video {video_id} during LLM generation: {str(e)}")

    logging.info("Pipeline Step 2B finished.")

if __name__ == '__main__':
    main()
    
    