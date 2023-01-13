from test1 import myapp

from fastapi.testclient import TestClient
client = TestClient(myapp)

def test_read_root():

    response = client.get('/')

    assert response.status_code=='200'
    assert response.json() == {"message": "hello world"}