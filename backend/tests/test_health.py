from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_retorna_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "modus-api"}


def test_openapi_mantem_metadados_da_api():
    schema = client.get("/openapi.json").json()

    assert schema["info"]["title"] == "Modus API"
    assert schema["info"]["version"] == "0.1.0"
    assert "/health" in schema["paths"]
