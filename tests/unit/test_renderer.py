"""Unit tests for the PlantUML renderer."""

from uml.plantuml_renderer import render_combined_puml

def test_render_combined_puml():
    """Tests that the combined PUML is rendered correctly."""
    class_puml = "@startuml\nclass A\n@enduml"
    sequence_puml = "@startuml\nAlice -> Bob: Hello\n@enduml"
    combined_puml = render_combined_puml(class_puml, sequence_puml)
    assert combined_puml == "@startuml\nclass A\n@enduml\n\n@startuml\nAlice -> Bob: Hello\n@enduml"
