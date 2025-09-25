from fastapi.testclient import TestClient
import main as appmod

client = TestClient(appmod.app)


def test_swagger_docs_loads():
    r = client.get("/docs")
    assert r.status_code == 200
    assert "Swagger" in r.text
