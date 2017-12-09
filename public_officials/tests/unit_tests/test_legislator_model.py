from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from unittest import skip
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
from django.contrib.auth.models import User
import vcr
from public_officials.helpers import test_helper as TestHelper
from public_officials.tests.factories import *

class LegislatorModelTest(TestCase):
    def test_a_legislators_attributes(self):
        legislator = Legislator()
        legislator.cid = "1234"
        legislator.state = "AZ"
        legislator.first_name = "Razz"
        legislator.last_name = "Fluff"
        legislator.phone = "1234456"
        legislator.email = "email@email.com"
        legislator.pid = "D000197"
        legislator.party = "R"
        legislator.chamber = "house"
        legislator.url = 'null.com/null/null.php'
        legislator.in_office = True

        legislator.save()

        saved_legislator = Legislator.objects.last()
        self.assertEqual(saved_legislator, legislator)
        self.assertEqual(saved_legislator.cid, "1234")
        self.assertEqual(saved_legislator.state, "AZ")
        self.assertEqual(saved_legislator.first_name, "Razz")
        self.assertEqual(saved_legislator.in_office, True)
        self.assertEqual(saved_legislator.leadership_role, None)

    @skip('fix later')
    def test_get_senators_by_state(self):
        legislator_one = LegislatorFactory.create(state='TX', chamber='senate')
        legislator_two = LegislatorFactory.create(state='AZ', chamber='senate')
        legislator_three = LegislatorFactory.create(state='CO', chamber='senate')
        legislator_four = LegislatorFactory.create(state='AZ', chamber='house')
        legislator_five = LegislatorFactory.create(state='AK', chamber='house')
        result = Legislator.get_senators_by_state()
        self.assertEqual(len(result), 3)
        self.assertEqual(legislator_one.id, result["Texas"].first().id)
        self.assertEqual(legislator_two.id, result["Arizona"].first().id)
        self.assertEqual(legislator_three.id, result["Colorado"].first().id)

    @skip('fix later')
    def test_get_representatives_by_state(self):
        legislator_one = LegislatorFactory.create(state='TX', chamber='house')
        legislator_two = LegislatorFactory.create(state='AZ', chamber='house')
        legislator_three = LegislatorFactory.create(state='CO', chamber='house')
        legislator_four = LegislatorFactory.create(state='AZ', chamber='senate')
        legislator_five = LegislatorFactory.create(state='AK', chamber='house')
        result = Legislator.get_representatives_by_state()
        self.assertEqual(len(result), 3)
        self.assertEqual(legislator_one.id, result["Texas"].first().id)
        self.assertEqual(legislator_two.id, result["Arizona"].first().id)
        self.assertEqual(legislator_two.id, result["Colorado"].first().id)

    @skip('fix later')
    def test_get_all_state_names(self):
        legislator_one = LegislatorFactory.create(state='TX', chamber='house')
        legislator_two = LegislatorFactory.create(state='AZ', chamber='house')
        legislator_three = LegislatorFactory.create(state='CO', chamber='house')
        legislator_four = LegislatorFactory.create(state='AZ', chamber='senate')
        legislator_five = LegislatorFactory.create(state='AK', chamber='house')
        returned_states = Legislator.get_all_state_names()
        self.assertEqual(4, len(returned_states))
        self.assertEqual('Alaska', returned_states[0])
        self.assertEqual('Arizona', returned_states[1])
        self.assertEqual('Colorado', returned_states[1])
        self.assertEqual('Texas', returned_states[1])
