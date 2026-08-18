import requests
import pytest
import time
class TestFhir:
    def _wait_until(self, endpoint,fhir_client,log_info, timeout=20):
        deadline = time.time() + timeout
        while (time.time() < deadline):
            res = fhir_client.get(endpoint)
            if res.status_code != 200:
                raise ValueError(f"invalid response check response, {res.status_code}")
            data = response.json()

            if data.status == "completed":
                return res
            time.sleep(5)

        raise ValueError(f"timed out not updated status as completed {data}")

    @pytest.mark.api_test
    def test_patient(self, fhir_client, log_info):
        patient_id = os.environ["FHIR_TEST_PATIENT_ID"]

        response = fhir_client.get_patient(patient_id)

        assert response.status_code == 200, (
            f"Patient lookup returned {response.status_code}"
        )

        patient = response.json()

        assert patient["resourceType"] == "Patient"
        assert patient["id"] == patient_id

    def test_search_by_family_name(self,fhir_client, log_info):
        patient_id="131707439"
        response = fhir_client.search_patient_by_family(patient_id)
        #response = requests.get(f"{BASE_URL}/patient/{patient_id}", params={"family":"smith"})

        assert response.status_code ==200
        resp = response.json()
        print(resp)
    
    def _refresh_auth_header(self) -> None:
    self.session.headers.pop("Authorization", None)
    self.session.headers.update(
        self.token_manager.get_authorization_header()
    )

    def get_patient(self, patient_id: str) -> requests.Response:
        self._refresh_auth_header()

        return self.session.get(
            f"{self.base_url}/Patient/{patient_id}",
            timeout=self.timeout,
        )