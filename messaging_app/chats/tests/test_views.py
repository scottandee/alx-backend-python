from rest_framework.test import APIClient
from rest_framework import status


def test_health_endpoint_no_db():
    client = APIClient()
    response = client.get("/api/health/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"status": "ok"}
