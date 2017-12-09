from public_officials.models import *
import factory
import datetime
import random
from faker import Faker
fake = Faker()

class LegislatorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Legislator
        abstract = False

    first_name = fake.name().split(' ')[0]
    last_name = fake.name().split(' ')[1]
    phone = fake.phone_number()
    email = fake.free_email()
    state = fake.country_code()
    cid = fake.postcode()
    pid = fake.postcode()
    chamber = random.choice(['senate', 'house'])
    party = random.choice(['R', 'D', 'I', 'G', 'L'])
    twitter_id = fake.user_name()
    leadership_role = random.choice([None, 'Leader', 'Other Leader'])
    govtrack_id = fake.postcode()
    cspan_id = fake.postcode()
    votesmart_id = fake.postcode()
    google_entity_id = fake.postcode()
    url = fake.url()
    in_office = random.choice([True, False, None])
