import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users():

    response = requests.get(
        f"{BASE_URL}/users"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0


def test_user_response_fields():

    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "email" in data