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
