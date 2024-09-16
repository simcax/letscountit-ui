"""Shared fixtures for tests."""

import pytest
from letscountitui import create_app


@pytest.fixture
def client():
    """Create a test client for the application."""
    app = create_app()
    app.config["FLASK_ENV"] = "development"
    app.config["SERVER_NAME"] = "localhost:5000"
    with app.app_context():
        with app.test_client() as client:
            yield client
