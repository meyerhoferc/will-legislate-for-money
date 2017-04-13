from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from public_officials.services import *
import pdb

class LegislatorDataTest(TestCase):

    def test_service_gets_legislator_information(self):
        self.assertEqual(Legislator.objects.count(), 0)
        legislator_service = LegislatorService()
        legislators = legislator_service.get_legislators_by_state("CO")
        self.assertEqual(Legislator.objects.count(), 9)
        legislator = Legislator.objects.first()
        self.assertTrue(legislator.name)
        self.assertTrue(legislator.state)
        self.assertTrue(legislator.cid)
