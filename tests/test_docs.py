from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_docs_alive():
    r = client.get("/docs")
    assert r.status_code in (200, 307, 308)
