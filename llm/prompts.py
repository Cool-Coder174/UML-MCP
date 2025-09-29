"""This module contains the prompt templates for the Gemini API."""

SYSTEM_PROMPT = """
You produce valid PlantUML for Class and Sequence diagrams. Always return compilable ` @startuml … @enduml`. Use concise names, proper multiplicities (`0..1`, `1..*`, etc.), composition/aggregation when implied, and correct arrows in sequences. If info is ambiguous, make reasonable defaults and document them in comments at the top of the output.
"""

USER_PROMPT_DOMAIN_JSON = """
Given the following domain JSON, generate a {diagram_type} diagram.

{domain_json}

Ensure the output starts with `@startuml` and ends with `@enduml`.
"""

USER_PROMPT_FREE_TEXT = """
Given the following free-form text, extract the entities, relationships, and interactions to generate a {diagram_type} diagram.

{free_text}

Ensure the output starts with `@startuml` and ends with `@enduml`.
"""
