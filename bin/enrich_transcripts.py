#!/usr/bin/env python3
import sys
import os
import json
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types
from abc import ABC, abstractmethod
import argparse

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
# 2. STRATEGY A: THE PRODUCTION GEMINI ENRICHER (Step 3 in LAB06a7)
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
def main(argv=None):
    """
    Main entry point for the transcript enrichment pipeline.
    Initializes the enrichment strategy and processes transcripts from stdin.
    """
    logging.info("Pipeline Step 2B (Gemini Enrichment) started.")
    parser = argparse.ArgumentParser(description="Transcript Enrichment Pipeline Node.")
    parser.add_argument(
        "--engine",
        choices=["gemini", "mock"],
        default="gemini",
    )
    args = parser.parse_args(argv)
    selected_strategy = GeminiStrategy()
    engine = TranscriptEnricher(selected_strategy)
    engine.run_stream()
    logging.info("Pipeline Step 2B finished.")
    
# =====================================================================
# 4. THE INVARIANT PIPELINE CONTEXT (The Streaming Engine) (Step 4 in LAB06a)
# =====================================================================
class TranscriptEnricher:
    """Streaming engine for transcript enrichment processing."""
    def __init__(self, strategy: LLMStrategy):
        self.strategy = strategy

    def run_stream(self):
        """Process incoming JSON lines from stdin and enrich transcripts."""
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            # ---------------------------------------------------------
            # Inbound line parsing — engine's responsibility, not the
            # strategy's. Malformed rows are logged and skipped.
            # ---------------------------------------------------------
            try:
                data = json.loads(line)
                video_id = data["video_id"]
                raw_text = data["raw_text"]
            except (json.JSONDecodeError, KeyError) as e:
                logging.error(f"Failed to parse incoming JSON payload row: {str(e)}")
                continue

            # ---------------------------------------------------------
            # Delegate the actual enrichment work to whatever strategy
            # was injected — engine has no idea if it's Gemini, Claude,
            # or a mock.
            # ---------------------------------------------------------
            try:
                result = self.strategy.enrich(video_id, raw_text)
                sys.stdout.write(json.dumps(result) + "\n")
                sys.stdout.flush()
            except ValueError as e:
                logging.error(f"Failed processing video {video_id} during enrichment: {str(e)}")
if __name__ == '__main__':
    main()
    
    