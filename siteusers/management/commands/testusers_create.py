import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from siteusers.models import SiteUsers


def load_from_json(file_name):
    with open(os.path.join(settings.BASE_DIR, f'siteusers/json/{file_name}.json'), encoding='UTF-8') as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = load_from_json('test_users')

        SiteUsers.objects.all().delete()
        for user in users:
            SiteUsers.objects.create(**user)

        #User.objects.get(username='django').delete()
        SiteUsers.objects.create_superuser('django', '123', 'geekbrains')
