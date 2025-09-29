"""Unit tests for the Gemini client."""

import pytest
from unittest.mock import patch, MagicMock
from llm.gemini_client import GeminiClient

@patch("google.generativeai.GenerativeModel")
@patch("google.generativeai.configure")
def test_gemini_client_generate_plantuml(mock_configure, mock_generative_model):
    """Tests that the Gemini client can generate PlantUML."""
    mock_model_instance = MagicMock()
    mock_generative_model.return_value = mock_model_instance
    mock_model_instance.generate_content.return_value.text = "@startuml\nclass A\n@enduml"

    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        mock_open.return_value.__enter__.return_value.readline.return_value = "test-api-key"
        client = GeminiClient()
        puml = client.generate_plantuml("a prompt")
        assert puml == "@startuml\nclass A\n@enduml"

def test_gemini_client_missing_key():
    """Tests that the Gemini client raises an error if the key is missing."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(RuntimeError):
            GeminiClient()
