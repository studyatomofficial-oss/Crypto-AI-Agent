from api.bybit import BybitClient


def test_bybit_client_initializes() -> None:
    client = BybitClient(api_key="key", api_secret="secret")
    assert client.api_key == "key"
    assert client.api_secret == "secret"
