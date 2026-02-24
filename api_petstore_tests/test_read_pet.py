from models import generate_pet

def test_get_existing_pet(client):
    pet = generate_pet()
    client.create_pet(pet)

    response = client.get_pet(pet["id"])

    assert response.status_code == 200
    assert response.json()["id"] == pet["id"]

def test_get_nonexistent_pet(client):
    response = client.get_pet(99999999999999)
    assert response.status_code == 404


def test_get_invalid_id(client):
    response = client.get_pet("abc")
    assert response.status_code == 404


def test_get_decimal_id(client):
    response = client.get_pet("1.5")
    assert response.status_code == 404


def test_get_negative_id(client):
    response = client.get_pet(-10)
    assert response.status_code != 200


def test_get_sql_injection_attempt(client):
    response = client.get_pet("1 OR 1=1")
    assert response.status_code != 200
