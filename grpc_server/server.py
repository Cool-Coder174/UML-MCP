"""This module contains the gRPC server implementation."""

from concurrent import futures
import grpc
from grpc_server.generated import uml_service_pb2
from grpc_server.generated import uml_service_pb2_grpc
def serve(test_mode=False):
    """Starts the gRPC server."""
    try:
        if test_mode:
            from llm.mock_gemini_client import MockGeminiClient as GeminiClient
        else:
            from llm.gemini_client import GeminiClient
        print(f"Using GeminiClient: {GeminiClient}")

        from mcp_server.mcp_tools import generate_uml

        class UMLService(uml_service_pb2_grpc.UMLServiceServicer):
            """The gRPC service for generating UML diagrams."""

            def GenerateUML(self, request, context):
                """Generates UML diagrams based on the provided request."""
                gemini_client = GeminiClient()
                result = generate_uml(
                    mode=request.mode,
                    payload=request.payload,
                    want_class=request.want_class,
                    want_sequence=request.want_sequence,
                    gemini_client=gemini_client,
                )
                return uml_service_pb2.GenerateUMLResponse(
                    class_puml=result["class_puml"],
                    sequence_puml=result["sequence_puml"],
                    combined_puml=result["combined_puml"],
                )

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        uml_service_pb2_grpc.add_UMLServiceServicer_to_server(UMLService(), server)
        server.add_insecure_port("[::]:50051")
        server.start()
        server.wait_for_termination()
    except Exception as e:
        with open("grpc_server.log", "a") as f:
            f.write(str(e))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    serve(test_mode=args.test)
