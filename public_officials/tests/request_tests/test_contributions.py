from django.test import TestCase
from public_officials.services import *
import vcr

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
