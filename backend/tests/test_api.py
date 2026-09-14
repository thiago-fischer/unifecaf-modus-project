import unittest

from fastapi.testclient import TestClient

from app.main import app


class ModusApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "service": "modus-api"})

    def test_models_catalog(self):
        response = self.client.get("/models")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("models", payload)
        self.assertEqual(len(payload["models"]), 3)
        self.assertEqual(payload["models"][0]["id"], "modus-economico")

    def test_simulate_valid_request(self):
        response = self.client.post(
            "/simulate",
            json={"modelId": "modus-equilibrado", "taskType": "summary", "responseSize": "medium"},
        )
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["tokens"]["input"], 800)
        self.assertEqual(payload["tokens"]["output"], 500)
        self.assertEqual(payload["tokens"]["total"], 1300)
        self.assertAlmostEqual(payload["cost"]["totalUsd"], 0.0069)
        self.assertEqual(payload["currency"], "USD")

    def test_simulate_invalid_model(self):
        response = self.client.post(
            "/simulate",
            json={"modelId": "modelo-inexistente", "taskType": "summary", "responseSize": "medium"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("modelo", response.json()["detail"]) 


if __name__ == "__main__":
    unittest.main()
