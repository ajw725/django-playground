import os
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from second_app.models import Topic, Webpage, AccessRecord

generator = Faker()
topic_names = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topic_names))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        topic = add_topic()
        url = generator.url()
        date = generator.date()
        name = generator.company()

        webpage = Webpage.objects.get_or_create(topic=topic, name=name, url=url)[0]
        webpage.save()

        access_record = AccessRecord.objects.get_or_create(name=webpage, date=date)[0]
        access_record.save()


if __name__ == '__main__':
    print('Seeding database...')
    populate(10)
    print('Seeding complete!')
