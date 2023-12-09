from faker import Faker

faker = Faker()

def get_registered_user():
    return {
        "name": faker.name(),
        "address": faker.address(),
        "phone": faker.phone_number,
        "job": faker.job(),
        "email": faker.email(),
        "company": faker.company(),
        "country": faker.country(),
        "city": faker.city(),
        "text": faker.text(),
        "state": faker.state(),
    }