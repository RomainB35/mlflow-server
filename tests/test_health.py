import requests

def test_mlflow_health():
    response = requests.get("http://localhost:8080/health")
    assert response.status_code == 200
