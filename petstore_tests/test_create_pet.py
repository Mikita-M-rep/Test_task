from models import generate_pet


def test_create_pet_positive(client):
    pet = generate_pet()

    response = client.create_pet(pet)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == pet["id"]
    assert body["name"] == pet["name"]

def test_create_pet_malformed_json(client):
    response = client.session.post(
        f"{client.base_url}/pet",
        data="{invalid}",
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 400


def test_create_pet_unsupported_media_type(client):
    response = client.session.post(
        f"{client.base_url}/pet",
        data="plain text",
        headers={"Content-Type": "text/plain"}
    )

    assert response.status_code == 415