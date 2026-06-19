import requests

class FHIRClient:
    def __init__(self):
        self.base_url="https://hapi.fhir.org/baseR4"


    def get_patient(self, patient_id):
        print( f"{self.base_url}/{patient_id}")
        return requests.get(
            f"{self.base_url}/Patient/{patient_id}"
        )