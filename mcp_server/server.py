"""This module contains the MCP server implementation."""

from mcp import MCP, Tool
from mcp_server.mcp_tools import generate_uml

class GenerateUMLTool(Tool):
    """A tool for generating UML diagrams."""
    name = "generate_uml"
    description = "Generates PlantUML code for class and sequence diagrams."
    input_schema = {
        "type": "object",
        "properties": {
            "mode": {"type": "string", "enum": ["domain_json", "free_text"]},
            "payload": {"type": "string"},
            "want_class": {"type": "boolean", "default": True},
            "want_sequence": {"type": "boolean", "default": True},
        },
        "required": ["mode", "payload"],
    }

    async def run(self, **kwargs) -> dict:
        """Runs the tool."""
        return generate_uml(**kwargs)

if __name__ == "__main__":
    mcp = MCP()
    mcp.add_tool(GenerateUMLTool())
    mcp.run()