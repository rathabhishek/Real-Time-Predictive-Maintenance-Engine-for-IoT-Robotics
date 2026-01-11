import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from services.inference_api.app import app

client = TestClient(app)

# Mocking the TensorFlow model to isolate API testing (DevOps Best Practice)
@pytest.fixture
def mock_model():
    with patch('tensorflow.keras.models.load_model') as mock_load:
        mock_instance = MagicMock()
        # Simulate a 95% probability of failure prediction
        mock_instance.predict.return_value = [[0.95]]
        mock_load.return_value = mock_instance
        yield mock_instance

def test_read_main():
    """Verify health check endpoint for K8s Liveness Probes"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "AegisML Online"}

def test_prediction_endpoint(mock_model):
    """Test the core ML inference route with simulated sensor window"""
    # Mocking a 50-step, 3-feature window
    test_data = [[0.1, 70.0, 220.0]] * 50 
    
    response = client.post("/predict", json=test_data)
    
    assert response.status_code == 200
    assert "failure_probability" in response.json()
    assert response.json()["failure_probability"] == 0.95