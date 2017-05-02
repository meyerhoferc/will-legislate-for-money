from django.core.management.base import BaseCommand, CommandError
from public_officials.models import *
from public_officials.services import *
import requests
import shutil

class Command(BaseCommand):
    def handle(self, *args, **options):
        legislators = Legislator.objects.all()
        for legislator in legislators:
            r = requests.get('https://theunitedstates.io/images/congress/225x275/' + legislator.pid + '.jpg', stream=True)
            if r.status_code == 200:
                with open('public_officials/static/public_officials/images/profiles/' + legislator.pid + '.jpg', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
