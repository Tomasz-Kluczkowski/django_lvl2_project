import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Lvl2_Project.settings')

import django
django.setup()

from users.models import User
from faker import Faker

fake = Faker()


def populator(n=10):
    """Populates User model with fake names and emails."""

    for item in range(n):

        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        # create new user out of the above fake data

        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]

if __name__ == "__main__":
    print("populating...")
    populator(50)
    print("finished populating")
