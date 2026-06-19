import requests
import pytest

class TestFhir:
    @pytest.mark.api_test
    def test_patient(self, fhir_client, log_info):
        patient = "131707439"
        response = fhir_client.get_patient(patient)
        assert response.status_code == 200
        patient_res = response.json()
        patien = patient_res["resourceType"]
        print(patient_res["meta"]["tag"][0]["system"])
        assert patient_res["resourceType"] =="Patient"
        assert patient_res["meta"]["versionId"] == "3"
        assert patient_res["meta"]["tag"][0]["system"] == "http://example.org/data-quality"
        assert patient_res["text"]["status"] == "generated"
        assert patient_res["name"][0]["family"] == "Williams"
        assert patient_res["address"][0]["line"][0] == "145 E 167th St, Room 4B"
        assert patient_res["communication"][0]["language"]["text"] == "Spanish"
        assert "Spanish" in  patient_res["communication"][0]["language"]["coding"][0].values()
        for c in patient_res.get("communication", []):
            assert c["language"]["coding"][0]["code"] == "es"
        log_info.info("where is my message ")
       
        

        assert patient_res["id"] == patient

    def test_search_by_family_name(self):
        patient_id="1234"
        response = requests.get(f"{BASE_URL}/patient/{patient_id}", params={"family":"smith"})

        assert response.status_code ==200
        resp = response.json()
        print(resp)