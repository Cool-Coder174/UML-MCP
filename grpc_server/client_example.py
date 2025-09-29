"""This module contains a gRPC client example."""

import grpc
from grpc_server.generated import uml_service_pb2
from grpc_server.generated import uml_service_pb2_grpc

def run():
    """Runs the gRPC client example."""
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
        print("Class PUML:", response.class_puml)
        print("Sequence PUML:", response.sequence_puml)

if __name__ == "__main__":
    run()
