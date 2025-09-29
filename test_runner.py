import pytest

if __name__ == '__main__':
    pytest.main(["-q", "tests/integration/test_cli_end_to_end.py", "tests/integration/test_grpc_roundtrip.py"])
