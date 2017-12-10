from django.core.management.base import BaseCommand, CommandError
from public_officials.models import *
from public_officials.services import *
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        legislators = Legislator.objects.all()
        for legislator in legislators:
            legislator.delete()
            self.stdout.write(self.style.SUCCESS('Successfully deleted legislator %s %s' % legislator.first_name, legislator.last_name))

        legislator_service = LegislatorService()
        senators = legislator_service.get_all_senators(115)
        for senator in senators:
            Legislator.objects.create(
            first_name=senator["first_name"],
            last_name=senator["last_name"],
            phone=senator["phone"],
            email=senator["contact_form"],
            state=senator["state"],
            cid=senator["crp_id"],
            pid=senator["id"],
            chamber='senate',
            party=senator["party"],
            twitter_id=senator.get("twitter_id"),
            leadership_role = senator["leadership_role"],
            govtrack_id = senator["govtrack_id"],
            cspan_id = senator["cspan_id"],
            url = senator["url"],
            in_office = senator["in_office"]
            )
            self.stdout.write(self.style.SUCCESS('Successfully created senator %s' % senator["last_name"]))

        representatives = legislator_service.get_all_representatives(115)
        for representative in representatives:
            Legislator.objects.create(
            first_name=representative["first_name"],
            last_name=representative["last_name"],
            phone=representative["phone"],
            email=representative["contact_form"],
            state=representative["state"],
            cid=representative["crp_id"],
            pid=representative["id"],
            chamber='house',
            party=representative["party"],
            twitter_id=representative.get("twitter_id"),
            leadership_role = representative["leadership_role"],
            govtrack_id = representative["govtrack_id"],
            cspan_id = representative["cspan_id"],
            url = representative["url"],
            in_office = representative["in_office"]
            )
            self.stdout.write(self.style.SUCCESS('Successfully created representative %s' % representative["last_name"]))
