from django.test import TestCase, RequestFactory
from selenium import webdriver
from public_officials.models import *
from public_officials.views import *
from unittest import skip
import vcr

class RegisteredUserTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    @skip('come back')
    def test_user_show_page_content(self):
        with vcr.use_cassette('cassettes/logged_in_user_show'):
            user = User.objects.create_user('fake-user', 'lemmon@thebeatles.com', 'johnpassword')
            user_homepage_request = self.factory.get('/acounts/profile/')
            user_homepage_request.user = user
            user_homepage_response = user_show(user_homepage_request)
            self.assertIn(b'Welcome fake-user!!!', user_homepage_response.content)
            self.assertIn(b'Logout', user_homepage_response.content)
            self.assertNotIn(b'Login with Twitter', user_homepage_response.content)

    @skip('come back')
    def test_user_legislator_followed_relationship_displayed(self):
        with vcr.use_cassette('cassettes/user_followed_legislators'):
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
                                                   cid="N00006134",
                                                   twitter_id="RepDianaDeGette")
            user = User.objects.create_user('fake-user', 'lemmon@thebeatles.com', 'johnpassword')
            legislator.users.add(user)

            user_homepage_request = self.factory.get('/acounts/profile/')
            user_homepage_request.user = user
            user_homepage_response = user_show(user_homepage_request)
            self.assertIn(b'Diana DeGette', user_homepage_response.content)
            self.assertIn(b'House', user_homepage_response.content)
            self.assertIn(b'CO-D', user_homepage_response.content)
            self.assertIn(b'Display Tweets from Diana', user_homepage_response.content)
            self.assertIn(b'Unfollow Diana', user_homepage_response.content)

            legislator_show_request = self.factory.get(f'/legislators/{legislator.id}')
            legislator_show_request.user = user
            legislator_show_response = legislator_detail(legislator_show_request, legislator.id)
            self.assertIn(b'Unfollow', legislator_show_response.content)
            self.assertNotIn(b'Follow', legislator_show_response.content)

            user.legislator_set.remove(legislator)
            user_homepage_request = self.factory.get('/acounts/profile/')
            user_homepage_request.user = user
            user_homepage_response = user_show(user_homepage_request)
            self.assertNotIn(b'Diana DeGette', user_homepage_response.content)
            self.assertNotIn(b'House', user_homepage_response.content)
            self.assertNotIn(b'CO-D', user_homepage_response.content)
            self.assertNotIn(b'Display Tweets from Diana', user_homepage_response.content)
            self.assertNotIn(b'Unfollow Diana', user_homepage_response.content)

            legislator_show_request = self.factory.get(f'/legislators/{legislator.id}')
            legislator_show_request.user = user
            legislator_show_response = legislator_detail(legislator_show_request, legislator.id)
            self.assertNotIn(b'Unfollow', legislator_show_response.content)
            self.assertIn(b'Follow', legislator_show_response.content)
