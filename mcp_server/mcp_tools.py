"""This module contains the implementation of the MCP tools."""

import json
from llm.gemini_client import GeminiClient
from llm.prompts import SYSTEM_PROMPT, USER_PROMPT_DOMAIN_JSON, USER_PROMPT_FREE_TEXT
from mcp_server.schemas import DomainModel
from uml.plantuml_renderer import render_combined_puml

def generate_uml(mode: str, payload: str, want_class: bool, want_sequence: bool, gemini_client: GeminiClient = None) -> dict:
    """
    Generates PlantUML code for class and sequence diagrams.

    Args:
        mode: The generation mode ("domain_json" or "free_text").
        payload: The input payload (JSON or plain text).
        want_class: Whether to generate a class diagram.
        want_sequence: Whether to generate a sequence diagram.

    Returns:
        A dictionary containing the generated PlantUML code.
    """
    if gemini_client is None:
        gemini_client = GeminiClient()
    class_puml = ""
    sequence_puml = ""

    if want_class:
        if mode == "domain_json":
            domain_model = DomainModel.parse_raw(payload)
            prompt = USER_PROMPT_DOMAIN_JSON.format(
                diagram_type="class", domain_json=domain_model.json()
            )
        else:
            prompt = USER_PROMPT_FREE_TEXT.format(
                diagram_type="class", free_text=payload
            )
        class_puml = gemini_client.generate_plantuml(f"{SYSTEM_PROMPT}\n{prompt}")

    if want_sequence:
        if mode == "domain_json":
            domain_model = DomainModel.parse_raw(payload)
            prompt = USER_PROMPT_DOMAIN_JSON.format(
                diagram_type="sequence", domain_json=domain_model.json()
            )
        else:
            prompt = USER_PROMPT_FREE_TEXT.format(
                diagram_type="sequence", free_text=payload
            )
        sequence_puml = gemini_client.generate_plantuml(f"{SYSTEM_PROMPT}\n{prompt}")

    combined_puml = ""
    if want_class and want_sequence:
        combined_puml = render_combined_puml(class_puml, sequence_puml)

    return {
        "class_puml": class_puml,
        "sequence_puml": sequence_puml,
        "combined_puml": combined_puml,
    }
