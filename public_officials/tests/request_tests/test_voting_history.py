from django.test import TestCase
from public_officials.services import *
import vcr

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
