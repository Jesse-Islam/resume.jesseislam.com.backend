# tests/test_main.py

import pytest
from main import app, doc_ref

@pytest.fixture(autouse=True)
def stub_doc_ref(monkeypatch):
    """
    Replace the real Firestore document with a dummy that:
    - ignores .set()
    - returns a fixed view_count on .get()
    """
    class DummyDoc:
        def set(self, data, merge=True):
            # no-op
            pass

        def get(self):
            class R:
                def to_dict(self_inner):
                    return {"view_count": 7}
            return R()

    monkeypatch.setattr("main.doc_ref", DummyDoc())

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_options_preflight(client):
    """OPTIONS / should return HTTP 200 and no body"""
    resp = client.open("/", method="OPTIONS")
    assert resp.status_code == 200
    assert resp.data == b""

def test_post_increments_and_returns_json(client):
    """POST / should return JSON with a 'view_count' key of 7"""
    resp = client.post("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert "view_count" in data
    assert data["view_count"] == 7
