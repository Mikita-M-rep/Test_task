from models import generate_pet

def test_update_pet_positive(client):
    pet = generate_pet()
    client.create_pet(pet)

    pet["name"] = "UpdatedName"
    pet["status"] = "sold"

    response = client.update_pet(pet)
    assert response.status_code == 200

    check = client.get_pet(pet["id"])
    assert check.json()["name"] == "UpdatedName"

def test_update_pet_malformed_json(client):
    response = client.session.put(
        f"{client.base_url}/pet",
        data="{invalid}",
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 400
