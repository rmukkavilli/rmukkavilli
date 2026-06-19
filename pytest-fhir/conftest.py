import pytest
import requests
from api_client import FHIRClient

@pytest.fixture
def fhir_client():
    return FHIRClient()

      # base_url = "https://fhir-service.example/fhir"
    # token = "you bearer token"

    # session = requests.Session()
    # session.headers.update({"Authorization": f"Bearer {token}",
    #     "Accept": "application/fhir+json",
    #     "Content-Type": "application/fhir+json"})