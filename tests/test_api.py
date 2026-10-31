from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={"criteria": ["Users can upload PDFs", "Maximum upload size is 10MB"]},
    )

    response_data = response.json()
    assert response.status_code == 200
    assert response_data["total"] == 2
    assert response_data["criteria"][0]["text"] == "Users can upload PDFs"


def test_analyze_endpoint_bad_request():
    response = client.post("/analyze", json={"criteria": "This is not a list!"})

    response_data = response.json()
    assert response.status_code == 422
    assert response_data["detail"][0]["loc"] == ["body", "criteria"]
