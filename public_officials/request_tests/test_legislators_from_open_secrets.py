from django.test import TestCase
from public_officials.services import *
import vcr

class LegislatorProfileDataTest(TestCase):

    def test_service_gets_all_legislators(self):
        with vcr.use_cassette('cassettes/get_sunlight_profile'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_legislators()
            legislator_attributes = legislators[0].keys()
            self.assertTrue(legislators)
            self.assertIn('chamber', legislator_attributes)
            self.assertIn('district', legislator_attributes)
            self.assertIn('first_name', legislator_attributes)
            self.assertIn('last_name', legislator_attributes)
            self.assertIn('party', legislator_attributes)
            self.assertIn('state', legislator_attributes)

class LegislatorContributionDataTest(TestCase):

    def test_service_gets_organizational_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_organizations'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_org_contributions("N00006134")
            contribution_attributes = legislator_contributions[0]['@attributes'].keys()
            self.assertTrue(legislator_contributions)
            self.assertIn('org_name', contribution_attributes)
            self.assertIn('total', contribution_attributes)
            self.assertIn('pacs', contribution_attributes)
            self.assertIn('indivs', contribution_attributes)
            self.assertEqual("Democracy Engine", legislator_contributions[0]['@attributes']['org_name'])

    def test_service_gets_industrial_contributions_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_legislator_industries'):
            legislator_service = LegislatorService()
            legislator_contributions = legislator_service.get_legislator_ind_contributions("N00006134")
            contribution_attributes = legislator_contributions[0]['@attributes'].keys()
            self.assertTrue(legislator_contributions)
            self.assertIn('industry_code', contribution_attributes)
            self.assertIn('industry_name', contribution_attributes)
            self.assertIn('indivs', contribution_attributes)
            self.assertIn('pacs', contribution_attributes)
            self.assertIn('total', contribution_attributes)

    def test_get_all_legislators_returns_all_legislators(self):
        with vcr.use_cassette('cassettes/get_all_legislators'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_legislators()
            legislator_attributes = legislators[0].keys()
            self.assertTrue(legislators)
            self.assertIn('chamber', legislator_attributes)
            self.assertIn('district', legislator_attributes)
            self.assertIn('first_name', legislator_attributes)
            self.assertIn('last_name', legislator_attributes)
            self.assertIn('term_start', legislator_attributes)
            self.assertIn('term_end', legislator_attributes)
            self.assertIn('party', legislator_attributes)
            self.assertIn('state', legislator_attributes)

class LegislatorSponsoredPolicyDataTest(TestCase):

    def test_service_gets_sponsored_bills_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_sponsored_bills'):
            legislator_service = LegislatorService()
            legislator_recent_bills = legislator_service.get_recent_bills('L000287')
            recent_bill_attributes = legislator_recent_bills[0].keys()
            self.assertTrue(legislator_recent_bills)
            self.assertIn('congress', recent_bill_attributes)
            self.assertIn('bill_id', recent_bill_attributes)
            self.assertIn('title', recent_bill_attributes)
            self.assertIn('sponsor_id', recent_bill_attributes)

class LegislatorVotingHistoryDataTest(TestCase):

    def test_service_gets_voting_history_for_one_legislator(self):
        with vcr.use_cassette('cassettes/get_vote_history'):
            legislator_service = LegislatorService()
            voting_history = legislator_service.get_voting_history('L000287')
            vote_history_attributes = voting_history[0].keys()
            self.assertTrue(voting_history)
            self.assertIn('member_id', vote_history_attributes)
            self.assertIn('chamber', vote_history_attributes)
            self.assertIn('congress', vote_history_attributes)
            self.assertIn('session', vote_history_attributes)
            self.assertIn('bill', vote_history_attributes)
            self.assertIn('description', vote_history_attributes)

class RecentVotesDataTest(TestCase):

    def test_service_gets_twenty_recent_bills(self):
        with vcr.use_cassette('cassettes/get_recent_bills'):
            bill_service = BillService()
            recent_bills = bill_service.get_recent_bills()
            recent_bill_attributes = recent_bills[0].keys()
            self.assertTrue(recent_bills)
            self.assertIn('bill_resolution_type', recent_bill_attributes)
            self.assertIn('congress', recent_bill_attributes)
            self.assertIn('is_alive', recent_bill_attributes)
            self.assertIn('link', recent_bill_attributes)
            self.assertIn('sponsor', recent_bill_attributes)
