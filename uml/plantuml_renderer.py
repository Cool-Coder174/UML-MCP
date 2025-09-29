"""This module contains the PlantUML renderer."""

def render_combined_puml(class_puml: str, sequence_puml: str) -> str:
    """
    Merges the class and sequence diagrams into a single PlantUML string.

    Args:
        class_puml: The class diagram PlantUML code.
        sequence_puml: The sequence diagram PlantUML code.

    Returns:
        The combined PlantUML code.
    """
    return f"{class_puml}\n\n{sequence_puml}"
