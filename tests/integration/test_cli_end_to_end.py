"""End-to-end tests for the CLI."""

import os
import subprocess

def test_cli_end_to_end():
    """Tests that the CLI can generate PUML files from a domain JSON."""
    outdir = "./test_out"
    subprocess.run([
        "python",
        "-m",
        "cli.main",
        "--mode",
        "domain_json",
        "--input",
        "examples/ecommerce_domain.json",
        "--class",
        "--sequence",
        "--outdir",
        outdir,
    ])
    assert os.path.exists(os.path.join(outdir, "class_diagram.puml"))
    assert os.path.exists(os.path.join(outdir, "sequence_diagram.puml"))
    assert os.path.exists(os.path.join(outdir, "uml_bundle.puml"))
