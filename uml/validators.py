"""Validators for the generated PlantUML code."""

import re

def validate_plantuml(puml_code: str):
    """
    Validates the generated PlantUML code.

    Args:
        puml_code: The PlantUML code to validate.

    Raises:
        ValueError: If the PlantUML code is invalid.
    """
    if not puml_code.startswith("@startuml"):
        raise ValueError("PlantUML code must start with @startuml")
    if not puml_code.endswith("@enduml"):
        raise ValueError("PlantUML code must end with @enduml")

def validate_class_name(class_name: str):
    """
    Validates a class name.

    Args:
        class_name: The class name to validate.

    Raises:
        ValueError: If the class name is invalid.
    """
    if not re.match(r"^[a-zA-Z0-9_]+$", class_name):
        raise ValueError(f"Invalid class name: {class_name}")

def validate_multiplicity(multiplicity: str):
    """
    Validates a multiplicity value.

    Args:
        multiplicity: The multiplicity value to validate.

    Raises:
        ValueError: If the multiplicity value is invalid.
    """
    known_multiplicities = ["0..1", "1", "0..*", "1..*", "*"]
    if multiplicity not in known_multiplicities:
        raise ValueError(f"Invalid multiplicity: {multiplicity}")
