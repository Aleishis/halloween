import app as app_module

def test_index_responde():
    client = app_module.test_client()
    assert client.get("/").status_code == 200