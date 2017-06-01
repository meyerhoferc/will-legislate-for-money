from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
from django.contrib.auth.models import User
import vcr

class LegislatorRelationshipsTest(TestCase):
    def test_legislator_has_many_to_many_relationship_with_users(self):
        legislator = Legislator.objects.create(first_name="Diana",
                                               last_name="DeGette",
                                               phone="12345",
                                               email="email@email.com",
                                               state_name="Colorado",
                                               pid="D000197",
                                               chamber="house",
                                               term_start="2017-01-03",
                                               term_end="2019-01-03",
                                               party="D",
                                               state="CO",
                                               cid="N00006134")
        legislator_two = Legislator.objects.create(first_name="Henry",
                                                   last_name="Schmojo",
                                                   phone="12345",
                                                   email="email@email.com",
                                                   state_name="Texas",
                                                   pid="D000197",
                                                   chamber="house",
                                                   term_start="2017-01-03",
                                                   term_end="2019-01-03",
                                                   party="D",
                                                   state="TX",
                                                   cid="N00006134")
        user = User.objects.create(username='test')
        user2 = User.objects.create(username='test2')

        legislator.users.add(user)
        legislator.users.add(user2)
        legislator_two.users.add(user)

        self.assertEqual(legislator.users.count(), 2)
        self.assertEqual(legislator_two.users.count(), 1)
        self.assertEqual(user.legislator_set.all().count(), 2)
        self.assertEqual(user2.legislator_set.all().count(), 1)
        self.assertEqual(user2.legislator_set.all().first(), legislator)
