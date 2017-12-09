from django.test import TestCase
from public_officials.services import *
import vcr

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
