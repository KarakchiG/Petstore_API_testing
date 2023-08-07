import random
from faker import Faker

fake = Faker()


def generate_pet_payload(**kwargs):
    return {
        "category": {
            "id": kwargs.get("id", 1),
            "name": kwargs.get("category_name", "Dog")
        },
        "name": kwargs.get("name", fake.name()),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Dog"
            }
        ],
        "status": kwargs.get("status", "available")
    }


# another example of payload generator
def generate_person_payload(**kwargs):
    payload = {
        "name": kwargs.get("name", fake.name()),
        "email": kwargs.get("email", fake.email()),
        "age": kwargs.get("age", random.randint(18, 65))
    }
    return payload

# payload = generate_person_payload(name="Hennadii Karakchi", email="k.gena@example.com")
# print(payload)
