import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns expected response."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "timestamp" in data
    assert "version" in data
    assert data["message"] == "Hello from Azure Container Apps!"
    assert data["version"] == "1.0.0"

def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "timestamp" in data
    assert "environment" in data
    assert data["status"] == "healthy"
    assert data["environment"] == "development"

def test_config_endpoint():
    """Test the configuration endpoint."""
    response = client.get("/config")
    assert response.status_code == 200
    data = response.json()
    assert "database_configured" in data
    assert "api_key_configured" in data
    assert "environment" in data
    assert isinstance(data["database_configured"], bool)
    assert isinstance(data["api_key_configured"], bool)

def test_invalid_endpoint():
    """Test that invalid endpoints return 404."""
    response = client.get("/invalid")
    assert response.status_code == 404

if __name__ == "__main__":
    # Run tests with simple output when executed directly
    print("Running FastAPI tests...\n")

    test_functions = [
        test_root_endpoint,
        test_health_endpoint,
        test_config_endpoint,
        test_invalid_endpoint
    ]

    passed = 0
    failed = 0

    for test_func in test_functions:
        try:
            test_func()
            print(f"✅ {test_func.__name__}: PASSED")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_func.__name__}: FAILED - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test_func.__name__}: ERROR - {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'='*50}")

    if failed > 0:
        exit(1)
    print("\n🎉 All tests passed!")