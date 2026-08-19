import time

import pytest


def patient_ids_from_bundle(bundle: dict) -> set[str]:
    return {
        entry.get("resource", {}).get("id")
        for entry in bundle.get("entry", [])
        if entry.get("resource", {}).get("resourceType") == "Patient"
    }


class TestFhir:
    @pytest.mark.api_test
    def test_patient(self, fhir_client, created_patient):
        patient_id = created_patient["id"]

        response = fhir_client.get_patient(patient_id)

        assert response.status_code == 200, (
            f"Patient lookup returned HTTP {response.status_code}"
        )

        patient = response.json()

        assert patient["resourceType"] == "Patient"
        assert patient["id"] == patient_id
        assert patient["name"][0]["family"] == created_patient["family_name"]

    @pytest.mark.api_test
    def test_search_by_family_name(self, fhir_client, created_patient):
        patient_id = created_patient["id"]
        family_name = created_patient["family_name"]

        for attempt in range(5):
            response = fhir_client.search_patient_by_family(family_name)

            assert response.status_code == 200, (
                f"Patient search returned HTTP {response.status_code}"
            )

            bundle = response.json()
            assert bundle["resourceType"] == "Bundle"

            if patient_id in patient_ids_from_bundle(bundle):
                return

            if attempt < 4:
                time.sleep(1)

        pytest.fail(
            "Created Patient did not appear in family-name search results"
        )