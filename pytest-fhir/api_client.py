import requests

from token_manager import TokenManager


class FHIRClient:
    def __init__(
        self,
        base_url: str,
        token_manager: TokenManager,
        timeout: float = 10.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.token_manager = token_manager
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/fhir+json",
                "Content-Type": "application/fhir+json",
            }
        )

    def _refresh_auth_header(self) -> None:
        self.session.headers.pop("Authorization", None)
        self.session.headers.update(
            self.token_manager.get_authorization_header()
        )

    def create_patient(self, patient: dict) -> requests.Response:
        self._refresh_auth_header()

        return self.session.post(
            f"{self.base_url}/Patient",
            json=patient,
            headers={"Prefer": "return=representation"},
            timeout=self.timeout,
        )

    def get_patient(self, patient_id: str) -> requests.Response:
        self._refresh_auth_header()

        return self.session.get(
            f"{self.base_url}/Patient/{patient_id}",
            timeout=self.timeout,
        )

    def search_patient_by_family(self, family_name: str) -> requests.Response:
        self._refresh_auth_header()

        return self.session.get(
            f"{self.base_url}/Patient",
            params={"family": family_name},
            timeout=self.timeout,
        )

    def delete_patient(self, patient_id: str) -> requests.Response:
        self._refresh_auth_header()

        return self.session.delete(
            f"{self.base_url}/Patient/{patient_id}",
            timeout=self.timeout,
        )