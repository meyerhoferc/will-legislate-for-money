from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from public_officials.services import *
import pdb
import vcr

class LegislatorProfileDataTest(TestCase):

    def test_service_gets_all_legislators(self):
        with vcr.use_cassette('cassettes/get_sunlight_profile'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_legislators()
            self.assertTrue(legislators)
            self.assertEqual(536, len(legislators))

class LegislatorContributionDataTest(TestCase):

    def test_service_gets_organizational_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_organizations'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_org_contributions("N00006134")
            self.assertTrue(legislator_contributions)
            self.assertEqual("Democracy Engine", legislator_contributions[0]['@attributes']['org_name'])

    def test_service_gets_industrial_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_industries'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_ind_contributions("N00006134")
            self.assertTrue(legislator_contributions)
            self.assertEqual("Pharmaceuticals/Health Products", legislator_contributions[0]['@attributes']['industry_name'])

    def test_get_all_legislators_returns_all_legislators(self):
        with vcr.use_cassette('cassettes/get_all_legislators'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_legislators()
            self.assertTrue(legislators)
            self.assertEqual("Luther", legislators[0]["first_name"])

class LegislatorSponsoredPolicyDataTest(TestCase):

    def test_service_gets_sponsored_bills_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_sponsored_bills'):
            legislator_service = LegislatorService()
            legislator_recent_bills = legislator_service.get_recent_bills('L000287')
            self.assertTrue(legislator_recent_bills)
            self.assertEqual("Missed Opportunities Act of 2017", legislator_recent_bills[0]["title"])

class LegislatorVotingHistoryDataTest(TestCase):
    
    def test_service_gets_voting_history_for_one_legislator(self):
        legislator_service = LegislatorService()
        voting_history = legislator_service.get_voting_history('L000287')
        self.assertTrue(voting_history)
        self.assertEqual("Supporting America's Innovators Act of 2017", voting_history[0]["title"])
        self.assertEqual("Yes", voting_history[0]["position"])
        self.assertEqual("Passed", voting_history[0]["result"])
