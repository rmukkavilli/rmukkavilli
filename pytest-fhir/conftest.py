from collections.abc import Iterator
import os
from uuid import uuid4

import pytest

from api_client import FHIRClient
from token_manager import TokenManager


@pytest.fixture(scope="session")
def token_manager() -> TokenManager:
    return TokenManager()


@pytest.fixture(scope="session")
def fhir_client(token_manager: TokenManager) -> FHIRClient:
    base_url = os.getenv("FHIR_BASE_URL") or "https://hapi.fhir.org/baseR4"
    return FHIRClient(
        base_url=base_url,
        token_manager=token_manager,
    )


@pytest.fixture(scope="module")
def created_patient(fhir_client: FHIRClient) -> Iterator[dict[str, str]]:
    unique_value = uuid4().hex
    family_name = f"Automation{unique_value}"

    patient_payload = {
        "resourceType": "Patient",
        "active": True,
        "identifier": [
            {
                "system": "https://example.test/patient-id",
                "value": unique_value,
            }
        ],
        "name": [
            {
                "use": "official",
                "family": family_name,
                "given": ["FHIRTest"],
            }
        ],
    }

    create_response = fhir_client.create_patient(patient_payload)
    assert create_response.status_code == 201, (
        "Patient creation returned "
        f"HTTP {create_response.status_code}"
    )

    created_resource = create_response.json()
    patient_id = created_resource.get("id")

    assert patient_id, "Created Patient response did not contain an id"

    try:
        yield {
            "id": patient_id,
            "family_name": family_name,
        }
    finally:
        delete_response = fhir_client.delete_patient(patient_id)
        assert delete_response.status_code in {200, 202, 204}, (
            "Patient cleanup returned "
            f"HTTP {delete_response.status_code}"
        )