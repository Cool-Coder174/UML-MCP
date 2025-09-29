"""Gemini client for interacting with the Google Gemini API."""

import os
import google.generativeai as genai

class GeminiClient:
    """A client for interacting with the Google Gemini API."""

    def __init__(self, api_key_path: str = "key.txt"):
        """
        Initializes the Gemini client.

        Args:
            api_key_path: The path to the file containing the API key.

        Raises:
            RuntimeError: If the API key file is missing or the key is empty.
        """
        try:
            with open(api_key_path, "r") as f:
                self.api_key = f.readline().strip()
            if not self.api_key:
                raise RuntimeError("Missing key.txt or empty API key")
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        except FileNotFoundError:
            raise RuntimeError("Missing key.txt or empty API key")

    def generate_plantuml(self, prompt: str) -> str:
        """
        Generates PlantUML code from a given prompt.

        Args:
            prompt: The prompt to send to the Gemini API.

        Returns:
            The generated PlantUML code.
        """
        response = self.model.generate_content(prompt)
        return response.text
