import sys
import io
import json
import pytest
from bin.enrich_transcripts import main, TranscriptEnricher, LLMStrategy
 
# 1. Build a dummy container mimicking the Gemini SDK response hierarchy
class MockGeminiResponse:
    def __init__(self, text_payload):
        self.text = text_payload
 
def test_enrich_transcripts_streaming_pipeline(monkeypatch, capsys):
    """
    Verifies that main() reads mock lines from stdin, calls the Gemini client structure,
    and streams verified JSON objects out to stdout without making live API network requests.
    """
    # 2. Mock out the core GenAI Client methods
    def mock_generate_content(self, model, contents, config=None):
        # Return a pre-baked, schema-compliant JSON string mimicking the model output
        mock_data = {
            "video_id": "ds5111_v001",
            "cleaned_text": "Welcome to class. Today we are testing mock frameworks.",
            "tech_terms": ["mock frameworks"],
            "book_names": []
        }
        return MockGeminiResponse(json.dumps(mock_data))
 
    # Corrected Module Target: Patch the actual Models service class inside the SDK
    from google.genai.models import Models
    monkeypatch.setattr(Models, "generate_content", mock_generate_content)
 
    # 3. Simulate your stream input pipeline using an in-memory text buffer
    mock_input_row = {"video_id": "ds5111_v001", "raw_text": "00:01 Welcome to class. Today we are testing mock frameworks."}
    mock_stdin = io.StringIO(json.dumps(mock_input_row) + "\n")
    monkeypatch.setattr(sys, "stdin", mock_stdin)
 
    # 4. Trigger the main pipeline script execution loop
    main(["--engine", "gemini"])
 
    # 5. Intercept the standard console text buffers
    captured = capsys.readouterr()
    stdout_lines = captured.out.strip().split("\n")
 
    # 6. Execute data integrity validation assertions
    assert len(stdout_lines) == 1
    parsed_output = json.loads(stdout_lines[0])
    assert parsed_output["video_id"] == "ds5111_v001"
    assert "mock frameworks" in parsed_output["tech_terms"]
    
# =====================================================================
# NEW TEST — exercises TranscriptEnricher directly via a local dummy
# strategy, bypassing main()/argparse/Gemini entirely.
# =====================================================================
class MockLLMStrategy(LLMStrategy):
    def enrich(self, video_id: str, raw_text: str) -> dict:
        return {
            "video_id": video_id,
            "cleaned_text": "Welcome to class. Today we are testing mock frameworks.",
            "tech_terms": ["mock frameworks"],
            "book_names": [],
        }


def test_transcript_enricher_streaming_pipeline(monkeypatch, capsys):
    """
    Verifies that TranscriptEnricher reads a line from stdin, delegates to
    the injected strategy, and streams a schema-compliant JSON object to
    stdout — without touching any real LLM vendor.
    """
    mock_input_row = {
        "video_id": "ds5111_v001",
        "raw_text": "00:01 Welcome to class. Today we are testing mock frameworks.",
    }
    mock_stdin = io.StringIO(json.dumps(mock_input_row) + "\n")
    monkeypatch.setattr(sys, "stdin", mock_stdin)

    engine = TranscriptEnricher(MockLLMStrategy())
    engine.run_stream()

    captured = capsys.readouterr()
    stdout_lines = captured.out.strip().split("\n")

    assert len(stdout_lines) == 1
    parsed_output = json.loads(stdout_lines[0])
    assert parsed_output["video_id"] == "ds5111_v001"
    assert "mock frameworks" in parsed_output["tech_terms"]