import requests


class HttpClient:
    def __init__(self, base_url: str = "") -> None:
        self.base_url = base_url

    def get(self, path: str, params: dict | None = None) -> dict:
        response = requests.get(f"{self.base_url}{path}", params=params, timeout=10)
        response.raise_for_status()
        return response.json()
