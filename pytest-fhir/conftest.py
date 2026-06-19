import pytest
import requests
import logging
from api_client import FHIRClient

@pytest.fixture
def fhir_client():
    return FHIRClient()

    
@pytest.fixture(scope="session")
def log_info():
    # logging.basicConfig(level=logging.INFO)
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    return logging.getLogger(__name__)



      # base_url = "https://fhir-service.example/fhir"
    # token = "you bearer token"

    # session = requests.Session()
    # session.headers.update({"Authorization": f"Bearer {token}",
    #     "Accept": "application/fhir+json",
    #     "Content-Type": "application/fhir+json"})