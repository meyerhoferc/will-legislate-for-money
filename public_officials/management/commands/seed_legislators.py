from django.core.management.base import BaseCommand, CommandError
from public_officials.models import *
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./public_officials/officials.csv') as legislators:
            read_legislators = csv.reader(legislators, delimiter=',')
            header = read_legislators.next()
            for row in read_legislators:
                Legislator.objects.create(
                name=row[0],
                cid=row[1],
                state=row[2],
                pid=row[3],
                first_elected=row[4],
                chamber=row[5],
                last_updated = row[6]
                )
                self.stdout.write(self.style.SUCCESS('Successfully created legislator %s' % row[0]))
