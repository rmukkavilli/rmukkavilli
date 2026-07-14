import pytest
import requests
import logging
from api_client import FHIRClient
from token_manager import TokenManager
import os

@pytest.fixture(scope="session")
def fhir_client(token_manager : TokenManager):
    base_url = os.getenv(
      "FHIR_BASE_URL",
      "https://hapi.fhir.org/baseR4",
    )
    return FHIRClient(base_url = base_url, token_manager = token_manager,)

@pytest.fixture(scope="session")
def token_manager() -> TokenManager:
  return TokenManager()
    
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