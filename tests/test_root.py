from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_ok():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("message") == "ok"

def test_root_content_type():
    r = client.get("/")
    assert r.headers["content-type"].startswith("application/json")
