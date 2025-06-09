import pytest
import mlflow
from mlflow.tracking import MlflowClient

def test_mlflow_server_connection():
    """Test que le serveur MLflow répond"""
    try:
        client = MlflowClient("http://localhost:8080")
        experiments = client.search_experiments()
        assert isinstance(experiments, list)
    except Exception as e:
        pytest.fail(f"Échec de connexion au serveur MLflow: {str(e)}")

def test_model_logging():
    """Test l'enregistrement d'un modèle"""
    with mlflow.start_run():
        mlflow.log_param("test_param", 42)
        logged_run = mlflow.active_run()
        assert logged_run is not None
        assert mlflow.get_run(logged_run.info.run_id).data.params["test_param"] == "42"
