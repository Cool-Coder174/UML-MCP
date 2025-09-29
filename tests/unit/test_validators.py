"""Unit tests for the PlantUML validators."""

import pytest
from uml.validators import validate_plantuml, validate_class_name, validate_multiplicity

def test_validate_plantuml():
    """Tests that the PlantUML validator works correctly."""
    with pytest.raises(ValueError):
        validate_plantuml("class A")
    with pytest.raises(ValueError):
        validate_plantuml("@startuml\nclass A")
    validate_plantuml("@startuml\nclass A\n@enduml")

def test_validate_class_name():
    """Tests that the class name validator works correctly."""
    with pytest.raises(ValueError):
        validate_class_name("invalid-class-name")
    validate_class_name("ValidClassName")
    validate_class_name("Valid_Class_Name")

def test_validate_multiplicity():
    """Tests that the multiplicity validator works correctly."""
    with pytest.raises(ValueError):
        validate_multiplicity("invalid-multiplicity")
    validate_multiplicity("0..1")
    validate_multiplicity("1")
    validate_multiplicity("0..*")
    validate_multiplicity("1..*")
    validate_multiplicity("*")
