import requests
from token_manager import TokenManager

class FHIRClient:
    def __init__(
        self,
        base_url: str,
        token_manager: TokenManager,
        timeout: float = 10.0,
    ):
        self.base_url=base_url.rstrip("/")
        self.token_manager = token_manager
        self.timeout = timeout
        

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/fhir+json",
                "Content-type": "application/fhir+json",
            }
        )
    def _refresh_auth_header(self) -> None:
        self.session.headers.pop("Authentication", None)
        self.session.headers.update(self.token_manager.get_authorization_header())

    def get_patient(self, patient_id: str) -> requests.Response:
        print( f"{self.base_url}/{patient_id}")
        return self.session.get(
            f"{self.base_url}/Patient/{patient_id}"
        )
    def search_patient_by_family(self,family_name: str) -> requests.Response:
        self._refresh_auth_header()

        return self.session.get(
            f"{self.base_url}/Patient",
            params={"family": family_name},
            timeout=self.timeout,
        )