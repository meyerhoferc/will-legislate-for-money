# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, RequestFactory
from django.core.handlers.wsgi import WSGIRequest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from public_officials.models import *
from public_officials.views import *
from mock import Mock, patch
import vcr
import os
import pdb

class RegisteredUserTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_show_page_content(self):
        with vcr.use_cassette('cassettes/logged_in_user_show'):
            user = User.objects.create_user('fake-user', 'lemmon@thebeatles.com', 'johnpassword')
            user_homepage_request = self.factory.get('/acounts/profile/')
            user_homepage_request.user = user
            user_homepage_response = user_show(user_homepage_request)
            self.assertIn(b'Welcome fake-user!!!', user_homepage_response.content)
            self.assertIn(b'Logout', user_homepage_response.content)
            self.assertNotIn(b'Login with Twitter', user_homepage_response.content)
            # pdb.set_trace()
            #
            # self.assertEqual(user.is_anonymous, False)
            # legislator = Legislator.objects.create(first_name="Diana",
            #                                        last_name="DeGette",
            #                                        phone="12345",
            #                                        email="email@email.com",
            #                                        state_name="Colorado",
            #                                        pid="D000197",
            #                                        chamber="house",
            #                                        term_start="2017-01-03",
            #                                        term_end="2019-01-03",
            #                                        party="D",
            #                                        state="CO",
            #                                        cid="N00006134",
            #                                        twitter_id="RepDianaDeGette")
            #
            # self.browser.get(self.live_server_url + '/legislators/%d/' % legislator.id)
            # follow_button_text = self.browser.find_element_by_css_selector('#follow-legislator').text
            # self.assertIn('Follow', follow_button_text)
            # self.browser.find_element_by_css_selector('.follow .btn').click()
            # self.assertIn('Unfollow', follow_button_text)
            # self.browser.get(self.live_server_url + '/accounts/profile/')
            # welcome_message = self.browser.find_element_by_css_selector('#welcome-message')
            # followed_legislators = self.browser.find_element_by_css_selector('#followed-legislators').text
            # self.assertIn('Diana DeGette', followed_legislators)
            # self.assertIn('House', followed_legislators)
            # self.assertIn('CO-D', followed_legislators)
