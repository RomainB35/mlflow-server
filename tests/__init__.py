# tests/__init__.py
from mlflow.tracking import MlflowClient
import pytest

__all__ = ['test_tracking', 'test_health']  # Liste des modules à importer
