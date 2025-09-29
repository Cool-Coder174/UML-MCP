"""Mock Gemini client for testing."""

class MockGeminiClient:
    """A mock client for the Gemini API."""

    def __init__(self, api_key_path: str = "key.txt"):
        """Initializes the mock Gemini client."""
        pass

    def generate_plantuml(self, prompt: str) -> str:
        """Generates a mock PlantUML diagram."""
        return "@startuml\nclass A\n@enduml"
