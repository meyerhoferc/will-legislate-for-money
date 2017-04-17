from django.core.management.base import BaseCommand, CommandError
from public_officials.models import *
from public_officials.services import *
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        legislator_service = LegislatorService()
        legislators = legislator_service.get_all_legislators
        for legislator in legislators:
            Legislator.objects.create(
            first_name=legislator["first_name"],
            last_name=legislator["last_name"],
            phone=legislator["phone"],
            email=legislator["oc_email"],
            state=legislator["state"],
            state_name=legislator["state_name"],
            cid=legislator["crp_id"],
            pid=legislator["bioguide_id"],
            chamber=legislator["chamber"],
            term_start=legislator["term_end"],
            term_end=legislator["term_start"],
            party=legislator["party"]
            )
            self.stdout.write(self.style.SUCCESS('Successfully created legislator %s' % row[0]))
