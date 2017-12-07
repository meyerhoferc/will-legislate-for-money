from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
from django.contrib.auth.models import User
import vcr

class LegislatorModelTest(TestCase):
    def test_a_legislators_attributes(self):
        legislator = Legislator()
        legislator.cid = "1234"
        legislator.state = "AZ"
        legislator.first_name = "Razz"
        legislator.last_name = "Fluff"
        legislator.phone = "1234456"
        legislator.email = "email@email.com"
        legislator.state_name = "Arizona"
        legislator.pid = "D000197"
        legislator.party = "R"
        legislator.chamber = "house"
        legislator.term_start = "2017-09-09"
        legislator.term_end = "2019-09-09"

        legislator.save()

        saved_legislator = Legislator.objects.last()
        self.assertEqual(saved_legislator, legislator)
        self.assertEqual(saved_legislator.cid, "1234")
        self.assertEqual(saved_legislator.state, "AZ")
        self.assertEqual(saved_legislator.first_name, "Razz")

    def test_get_senators_by_state(self):
        legislator_one = Legislator.objects.create(first_name="Diana",
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
                                                   chamber="senate",
                                                   term_start="2017-01-03",
                                                   term_end="2019-01-03",
                                                   party="D",
                                                   state="TX",
                                                   cid="N00006134")
        legislator_three = Legislator.objects.create(first_name="Love",
                                                     last_name="Fluff",
                                                     phone="12345",
                                                     email="email@email.com",
                                                     state_name="Colorado",
                                                     pid="D000197",
                                                     chamber="senate",
                                                     term_start="2017-01-03",
                                                     term_end="2019-01-03",
                                                     party="D",
                                                     state="CO",
                                                     cid="N00006134")
        legislator_four = Legislator.objects.create(first_name="Another",
                                                    last_name="Fluff",
                                                    phone="12345",
                                                    email="email@email.com",
                                                    state_name="Colorado",
                                                    pid="D000197",
                                                    chamber="senate",
                                                    term_start="2017-01-03",
                                                    term_end="2019-01-03",
                                                    party="D",
                                                    state="CO",
                                                    cid="N00006134")

        result = Legislator.get_senators_by_state()
        self.assertEqual(legislator_two.id, result["Texas"].first().id)
        self.assertEqual(legislator_three.id, result["Colorado"].first().id)

    def test_get_representatives_by_state(self):
        legislator_one = Legislator.objects.create(first_name="Diana",
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
        legislator_three = Legislator.objects.create(first_name="Love",
                                                     last_name="Fluff",
                                                     phone="12345",
                                                     email="email@email.com",
                                                     state_name="Colorado",
                                                     pid="D000197",
                                                     chamber="senate",
                                                     term_start="2017-01-03",
                                                     term_end="2019-01-03",
                                                     party="D",
                                                     state="CO",
                                                     cid="N00006134")
        legislator_four = Legislator.objects.create(first_name="Another",
                                                    last_name="Fluff",
                                                    phone="12345",
                                                    email="email@email.com",
                                                    state_name="Colorado",
                                                    pid="D000197",
                                                    chamber="senate",
                                                    term_start="2017-01-03",
                                                    term_end="2019-01-03",
                                                    party="D",
                                                    state="CO",
                                                    cid="N00006134")

        result = Legislator.get_representatives_by_state()
        self.assertEqual(legislator_one.id, result["Colorado"].first().id)
        self.assertEqual(legislator_two.id, result["Texas"].first().id)

    def test_get_all_state_names(self):
        legislator_one = Legislator.objects.create(first_name="Diana",
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
        legislator_three = Legislator.objects.create(first_name="Love",
                                                     last_name="Fluff",
                                                     phone="12345",
                                                     email="email@email.com",
                                                     state_name="Colorado",
                                                     pid="D000197",
                                                     chamber="senate",
                                                     term_start="2017-01-03",
                                                     term_end="2019-01-03",
                                                     party="D",
                                                     state="CO",
                                                     cid="N00006134")
        legislator_four = Legislator.objects.create(first_name="Another",
                                                    last_name="Fluff",
                                                    phone="12345",
                                                    email="email@email.com",
                                                    state_name="Colorado",
                                                    pid="D000197",
                                                    chamber="senate",
                                                    term_start="2017-01-03",
                                                    term_end="2019-01-03",
                                                    party="D",
                                                    state="CO",
                                                    cid="N00006134")
        returned_states = Legislator.get_all_state_names()
        self.assertEqual(2, len(returned_states))
        self.assertEqual('Colorado', returned_states[0])
        self.assertEqual('Texas', returned_states[1])
