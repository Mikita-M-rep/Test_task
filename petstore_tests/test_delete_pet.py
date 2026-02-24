from models import generate_pet

def test_delete_pet_positive(client):
    pet = generate_pet()
    client.create_pet(pet)

    response = client.delete_pet(pet["id"])
    assert response.status_code == 200

    check = client.get_pet(pet["id"])
    assert check.status_code == 404

def test_delete_nonexistent_pet(client):
    response = client.delete_pet(99999999999999)
    assert response.status_code == 404


def test_delete_invalid_id(client):
    response = client.delete_pet("abc")
    assert response.status_code == 404


def test_delete_negative_id(client):
    response = client.delete_pet(-1)
    assert response.status_code != 200


def test_delete_missing_path_parameter(client):
    response = client.session.delete(f"{client.base_url}/pet/")
    assert response.status_code in [404, 405]