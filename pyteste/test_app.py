import pytest
from app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_index(client):
    client.