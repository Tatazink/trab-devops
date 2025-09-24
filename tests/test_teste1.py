from fastapi.testclient import TestClient
import main as appmod
client = TestClient(appmod.app)

def test_teste1_status():
    assert client.get("/teste1").status_code == 200

def test_teste1_payload():
    body = client.get("/teste1").json()
    assert "teste" in body and body["teste"]