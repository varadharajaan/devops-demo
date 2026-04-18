import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test that home page returns 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint(client):
    """Test that health check returns 200 with expected JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_error_endpoint(client):
    """Test that error demo endpoint returns 500."""
    response = client.get("/error")
    assert response.status_code == 500
    data = response.get_json()
    assert data["status"] == "error"


# ============================================================
# INTENTIONAL FAILING TEST — for CI/CD demo
# Step 1: Push with this test → CI fails (red build)
# Step 2: Fix the assertion below (change 201 to 200) → push again → CI passes (green build)
# Step 3: Delete or keep this test as needed
# ============================================================
def test_health_returns_correct_code(client):
    """This test INTENTIONALLY FAILS to demo a broken build."""
    response = client.get("/health")
    # BUG: health returns 200, but we assert 201 — causes CI failure!
    assert response.status_code == 201, "Expected 201 but got 200 — fix this to 200 to pass!"
