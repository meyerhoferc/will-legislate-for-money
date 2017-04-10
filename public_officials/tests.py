from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'public-officials/home.html')
