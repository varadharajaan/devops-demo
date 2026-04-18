import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


# ============================================================
# INTENTIONAL FAILING TEST — for CI/CD demo
# Step 1: Push with this test → CI fails (red build)
# Step 2: Fix 201 to 200 → push again → CI passes (green build)
# ============================================================
def test_health_returns_correct_code(client):
    response = client.get("/health")
    # BUG: health returns 200, but we assert 201 — causes CI failure!
    assert response.status_code == 201, "Expected 201 but got 200 — fix this to 200 to pass!"
