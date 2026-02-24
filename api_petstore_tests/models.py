import time

def generate_pet(pet_id=None):
    return {
        "id": pet_id or int(time.time() * 1000),
        "name": "TestPet",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["string"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
    }