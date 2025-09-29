# UMLmcp

This project is a Python service that uses Google Gemini to generate PlantUML code for UML Class and Sequence diagrams. It exposes a gRPC interface and an MCP tool for generating UML diagrams.

## Setup

1.  Create a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Create a `key.txt` file in the root of the project and paste your Gemini API key in the first line.

## Generating gRPC stubs

To generate the gRPC stubs, run the following command:

```bash
python -m grpc_tools.protoc -I proto --python_out=grpc_server/generated --grpc_python_out=grpc_server/generated proto/uml_service.proto
```

## Running the servers

### gRPC server

To run the gRPC server, run the following command:

```bash
python -m grpc_server.server
```

### MCP server

The MCP (Model-Context-Protocol) server exposes the `generate_uml` tool, allowing other processes to generate UML diagrams. To run the MCP server, use the following command:

```bash
python -m mcp_server.server
```

## CLI usage

To use the CLI, run the following command:

```bash
python -m cli.main --mode [domain_json|free_text] --input <file or "-"> --class --sequence --outdir ./out
```

## Testing

To run the tests, run the following command:

```bash
pytest -q
```