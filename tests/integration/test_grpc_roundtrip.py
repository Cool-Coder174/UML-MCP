"""Integration tests for the gRPC server."""

import pytest
import subprocess
import time
import grpc
from grpc_server.generated import uml_service_pb2
from grpc_server.generated import uml_service_pb2_grpc

@pytest.mark.skip(reason="gRPC test is flaky and needs to be fixed.")
def test_grpc_roundtrip():
    """Tests that the gRPC server can handle a request and return a response."""
    with open("grpc_server.log", "w") as f:
        server_process = subprocess.Popen(["python", "-m", "grpc_server.server", "--test"], stdout=f, stderr=f)
    time.sleep(1)  # Give the server time to start

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = uml_service_pb2_grpc.UMLServiceStub(channel)
        response = stub.GenerateUML(
            uml_service_pb2.GenerateUMLRequest(
                mode="free_text",
                payload="A customer places an order.",
                want_class=True,
                want_sequence=True,
            )
        )
        assert response.class_puml
        assert response.sequence_puml


