"""Tests the basic routes of the application"""


def test_root_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Let's Count IT!" in response.data
