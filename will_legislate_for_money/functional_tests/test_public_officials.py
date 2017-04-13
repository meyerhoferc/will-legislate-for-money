from django.test import LiveServerTestCase
import time
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import vcr

class GuestUserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_check_for_correct_content_on_root(self):
        with vcr.use_cassette('cassettes/get_legislators'):
            self.browser.get(self.live_server_url)
            self.assertIn('Will Legislate For Money', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Your One Stop Corruption Watch', header_text)
            politician_text = self.browser.find_element_by_id('politicians').text
            self.assertIn("Diana DeGette", politician_text)
            self.assertIn("Jared Polis", politician_text)
            self.assertIn("Scott Tipton", politician_text)
