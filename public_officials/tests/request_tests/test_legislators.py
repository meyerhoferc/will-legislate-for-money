from django.test import TestCase
from public_officials.services import *
from unittest import skip
import vcr

class LegislatorProfileDataTest(TestCase):
    def test_service_gets_all_senators(self):
        with vcr.use_cassette('cassettes/get_all_senators_propublica'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_senators()
            legislator_attributes = legislators[0].keys()
            self.assertTrue(legislators)
            self.assertIn('first_name', legislator_attributes)
            self.assertIn('last_name', legislator_attributes)
            self.assertIn('party', legislator_attributes)
            self.assertIn('state', legislator_attributes)
            self.assertIn('leadership_role', legislator_attributes)
            self.assertIn('in_office', legislator_attributes)

    def test_service_gets_all_representatives(self):
        with vcr.use_cassette('cassettes/get_all_representatives_propublica'):
            legislator_service = LegislatorService()
            legislators = legislator_service.get_all_representatives()
            legislator_attributes = legislators[0].keys()
            self.assertTrue(legislators)
            self.assertIn('first_name', legislator_attributes)
            self.assertIn('last_name', legislator_attributes)
            self.assertIn('party', legislator_attributes)
            self.assertIn('state', legislator_attributes)
            self.assertIn('leadership_role', legislator_attributes)
            self.assertIn('in_office', legislator_attributes)

    @skip('add after data modeling complete')
    def test_service_gets_a_legislator_profile(self):
        with vcr.use_cassette('cassettes/get_legislator_profile_from_propublica'):
            legislator = LegislatorFactory.create(pid="KNOWN PROPUBLICA ID")
            legislator_service = LegislatorService()
            profile = legislator_service.get_profile_information_from_propublica(pid)
            legislator_attributes = legislator.keys()
            self.assertTrue(legislator)
            # other assertions to add after data modeling
