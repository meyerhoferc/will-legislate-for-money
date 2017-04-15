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

    def test_service_gets_profile_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_profile'):
            self.assertEqual(Legislator.objects.count(), 0)
            legislator_service = LegislatorService()
            legislator_profile = legislator_service.get_legislator_profile("N00006134")
            self.assertEqual(Legislator.objects.count(), 1)
            saved_legislator = Legislator.objects.first()
            self.assertEqual("DeGette, Diana", saved_legislator.name)
            self.assertEqual("N00006134", saved_legislator.cid)
            self.assertEqual("CO", saved_legislator.state)
            self.assertEqual("H", legislator_profile["chamber"])
            self.assertEqual("2016", legislator_profile["cycle"])
            self.assertEqual("1996", legislator_profile["first_elected"])

    def test_service_gets_organizational_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_organizations'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_org_contributions("N00006134")
            self.assertTrue(legislator_contributions)
            self.assertEqual("Democracy Engine", legislator_contributions[0]['@attributes']['org_name'])
