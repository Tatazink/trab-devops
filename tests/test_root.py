from fastapi.testclient import TestClient
import main as appmod
client = TestClient(appmod.app)

def test_root_status():
    assert client.get("/").status_code == 200

def test_root_payload():
    assert client.get("/").json() == {"message": "Hello World"}