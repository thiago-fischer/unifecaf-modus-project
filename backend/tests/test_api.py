from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_still_works():
    assert client.get("/health").json() == {"status": "ok", "service": "modus-api"}


def test_catalog_lists_options():
    body = client.get("/catalog").json()
    assert [m["id"] for m in body["models"]] == [
        "modus-economico",
        "modus-equilibrado",
        "modus-avancado",
    ]
    assert len(body["taskTypes"]) == 4
    assert len(body["responseSizes"]) == 3
    assert body["currency"] == "USD"


def test_simulation_returns_estimate_comparison_and_guidance():
    response = client.post(
        "/simulations",
        json={"modelId": "modus-equilibrado", "taskType": "summary", "responseSize": "medium"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["estimate"]["inputTokens"] == 800
    assert body["estimate"]["outputTokens"] == 500
    assert body["estimate"]["totalTokens"] == 1300
    assert body["estimate"]["cost"] == 0.0069
    assert body["currency"] == "USD"
    assert body["isEstimate"] is True
    assert [c["cost"] for c in body["comparison"]] == [0.00115, 0.0069, 0.023]
    assert [c["selected"] for c in body["comparison"]] == [False, True, False]
    assert body["guidance"] and body["disclaimer"]


def test_simulation_with_invalid_model_returns_clear_error():
    response = client.post(
        "/simulations",
        json={"modelId": "xyz", "taskType": "summary", "responseSize": "medium"},
    )
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail["code"] == "invalid_model"
    assert "xyz" in detail["message"]


def test_simulation_with_missing_field_is_rejected():
    response = client.post("/simulations", json={"modelId": "modus-economico"})
    assert response.status_code == 422
