from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from public_officials.services import *
import pdb
import vcr

class LegislatorDataTest(TestCase):

    def test_service_gets_legislator_information(self):
        with vcr.use_cassette('cassettes/get_legislators'):
            self.assertEqual(Legislator.objects.count(), 0)
            legislator_service = LegislatorService()
            legislators = legislator_service.get_legislators_by_state("CO")
            self.assertEqual(Legislator.objects.count(), 9)
            legislator = Legislator.objects.first()
            self.assertTrue(legislator.name)
            self.assertTrue(legislator.state)
            self.assertTrue(legislator.cid)
