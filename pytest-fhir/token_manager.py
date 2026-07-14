import os

class TokenManager:
    def __init__(self, access_token: str| None = None):
        self._access_token = access_token or os.getenv("FHIR_ACCESS_TOKEN")

    def get_access_token(self) -> str | None:
        return self._access_token

    def get_authorization_header(self) -> dict[str, str]:
        token = self.get_access_token()

        if not token:
            return {}
        
        return {"Authorization": f"Bearer {token}"}

