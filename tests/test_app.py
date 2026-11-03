from flask.app import app

def test_index_responde():
    client = app.test_client()
    assert client.get("/").status_code == 200