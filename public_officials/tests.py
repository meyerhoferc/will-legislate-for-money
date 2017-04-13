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

    def test_home_page_returns_correct_html(self):
        with vcr.use_cassette('cassettes/get_legislators'):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'public-officials/home.html')

class LegislatorModelTest(TestCase):
    def test_a_legislators_attributes(self):
        legislator = Legislator()
        legislator.cid = "1234"
        legislator.state = "AZ"
        legislator.name = "Razz Fluff"
        legislator.save()

        saved_legislator = Legislator.objects.last()
        self.assertEqual(saved_legislator, legislator)
        self.assertEqual(saved_legislator.cid, "1234")
        self.assertEqual(saved_legislator.state, "AZ")
        self.assertEqual(saved_legislator.name, "Razz Fluff")
