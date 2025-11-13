import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["version"] == "1.1.0"
    assert "message" in data
    assert data["timestamp"].endswith("Z")


def test_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    products = response.get_json()
    assert len(products) == 2
    for product in products:
        assert product["price"] > 0


def test_environment_endpoint(client, monkeypatch):
    monkeypatch.setenv("CODESPACES", "true")
    monkeypatch.setenv("GITHUB_WORKSPACE", "/workspaces/cicd-demo")

    response = client.get("/environment")
    assert response.status_code == 200

    data = response.get_json()
    assert data["codespaces"] is True
    assert data["workspace"] == "/workspaces/cicd-demo"
    assert data["python_version"]
