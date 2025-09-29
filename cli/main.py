"""This module contains the CLI for generating PlantUML diagrams."""

import argparse
import os
import sys
import os
if os.environ.get("TESTING") == "True":
    from llm.mock_gemini_client import MockGeminiClient as GeminiClient
else:
    from llm.gemini_client import GeminiClient

from mcp_server.mcp_tools import generate_uml

def main():
    """The main function for the CLI."""
    parser = argparse.ArgumentParser(description="Generate PlantUML diagrams.")
    parser.add_argument("--mode", choices=["domain_json", "free_text"], required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--class", dest="want_class", action="store_true")
    parser.add_argument("--no-class", dest="want_class", action="store_false")
    parser.add_argument("--sequence", dest="want_sequence", action="store_true")
    parser.add_argument("--no-sequence", dest="want_sequence", action="store_false")
    parser.add_argument("--outdir", default="./out")
    parser.set_defaults(want_class=True, want_sequence=True)
    args = parser.parse_args()

    if args.input == "-":
        payload = sys.stdin.read()
    else:
        with open(args.input, "r") as f:
            payload = f.read()

    gemini_client = GeminiClient()
    result = generate_uml(
        mode=args.mode,
        payload=payload,
        want_class=args.want_class,
        want_sequence=args.want_sequence,
        gemini_client=gemini_client,
    )

    os.makedirs(args.outdir, exist_ok=True)

    if args.want_class:
        with open(os.path.join(args.outdir, "class_diagram.puml"), "w") as f:
            f.write(result["class_puml"])

    if args.want_sequence:
        with open(os.path.join(args.outdir, "sequence_diagram.puml"), "w") as f:
            f.write(result["sequence_puml"])

    if args.want_class and args.want_sequence:
        with open(os.path.join(args.outdir, "uml_bundle.puml"), "w") as f:
            f.write(result["combined_puml"])

if __name__ == "__main__":
    main()
