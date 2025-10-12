from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_teste1_ok():
    r = client.get("/teste1")
    assert r.status_code == 200
    assert r.json().get("status") == "running"

def test_teste1_content_type():
    r = client.get("/teste1")
    assert r.headers["content-type"].startswith("application/json")