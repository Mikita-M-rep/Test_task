class PetApiClient:

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def create_pet(self, payload):
        return self.session.post(f"{self.base_url}/pet", json=payload)

    def get_pet(self, pet_id):
        return self.session.get(f"{self.base_url}/pet/{pet_id}")

    def update_pet(self, payload):
        return self.session.put(f"{self.base_url}/pet", json=payload)

    def delete_pet(self, pet_id):
        return self.session.delete(f"{self.base_url}/pet/{pet_id}")