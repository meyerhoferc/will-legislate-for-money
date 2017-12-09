from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
from django.contrib.auth.models import User
from unittest import skip
import vcr

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    @skip('come back')
    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'public-officials/home.html')

class StatePageTest(TestCase):

    @skip('come back')
    def test_state_url_resolves_to_state_view(self):
        found = resolve('/state/')
        self.assertEqual(found.func, state_legislators)

    @skip('come back')
    def test_state_legislators_returns_correct_template(self):
        response = self.client.get('/state/?state=Texas')
        self.assertTemplateUsed(response, 'public-officials/state.html')

class DetailPageTest(TestCase):
    @skip('come back')
    def test_detail_url_resolves_to_legislator_detail_view(self):
        found = resolve('/legislators/1/')
        self.assertEqual(found.func, legislator_detail)

    @skip('come back')
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
    @skip('come back')
    def test_senators_url_resolves_to_senators_index(self):
        found = resolve('/senators/')
        self.assertEqual(found.func, senator_index)

    @skip('come back')
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

    @skip('come back')
    def test_senators_url_resolves_to_senators_index(self):
        found = resolve('/representatives/')
        self.assertEqual(found.func, representative_index)

    @skip('come back')
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

class RecentBillsPageTest(TestCase):

    # @skip('come back')
    def test_recent_bills_url_resolves_to_bills_index_view(self):
        found = resolve('/recent-bills/')
        self.assertEqual(found.func, bills_index)

    # @skip('come back')
    def test_recent_bills_url_renders_correct_template(self):
        response = self.client.get('/recent-bills/')
        self.assertTemplateUsed(response, 'public-officials/bills/index.html')
