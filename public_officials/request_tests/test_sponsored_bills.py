from django.test import TestCase
from public_officials.services import *
import vcr

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
