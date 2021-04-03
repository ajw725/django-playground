import os
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from second_app.models import User

generator = Faker()


def populate(n=5):
    for entry in range(n):
        first_name = generator.first_name()
        last_name = generator.last_name()
        email = generator.email()
        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        user.save()


if __name__ == '__main__':
    print('Seeding users...')
    populate(10)
    print('Seeding users complete!')
