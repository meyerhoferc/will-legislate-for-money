from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
import vcr

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'public-officials/home.html')

class DetailPageTest(TestCase):
    def test_detail_url_resolves_to_legislator_detail_view(self):
        found = resolve('/legislators/1/')
        self.assertEqual(found.func, legislator_detail)

    def test_legislator_detail_page_returns_correct_template(self):
        with vcr.use_cassette('cassettes/get_complete_legislator_profile'):
            legislator = Legislator.objects.create(first_name="Diana",
                                                   last_name="Degette",
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

            response = self.client.get('/legislators/%d/' % legislator.id)
            self.assertTemplateUsed(response, 'public-officials/detail.html')

class SenatorPageTest(TestCase):
    def test_senators_url_resolves_to_senators_index(self):
        found = resolve('/senators/')
        self.assertEqual(found.func, senator_index)

    def test_senator_index_page_returns_correct_template(self):
        Legislator.objects.create(first_name="Diana",
                                  last_name="Degette",
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
        response = self.client.get('/senators/')
        self.assertTemplateUsed(response, 'public-officials/senators/index.html')

class RepresentativePageTest(TestCase):
    def test_senators_url_resolves_to_senators_index(self):
        found = resolve('/representatives/')
        self.assertEqual(found.func, representative_index)

    def test_senator_index_page_returns_correct_template(self):
        Legislator.objects.create(first_name="Diana",
                                  last_name="Degette",
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
        response = self.client.get('/representatives/')
        self.assertTemplateUsed(response, 'public-officials/representatives/index.html')


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
        expected_result = {"Texas": legislator_one, "Colorado": [legislator_three, legislator_four]}
        self.assertEqual(expected_result, Legislator.get_senators_by_state)
