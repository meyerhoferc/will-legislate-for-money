from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from public_officials.models import *
import os
import vcr

class GuestUserTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_check_for_correct_content_on_root(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Will Legislate For Money', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your One Stop Legislator Watch', header_text)
        selection_text = self.browser.find_element_by_css_selector('.selections').text
        self.assertIn("View Senators", selection_text)
        self.assertIn("View Representatives", selection_text)
        self.assertIn("View by State", selection_text)


    def test_has_link_to_view_recent_bills_and_that_content(self):
        self.browser.get(self.live_server_url)
        navbar_text = self.browser.find_element_by_css_selector('.navbar').text
        self.assertIn("Recent Bills", navbar_text)
        self.browser.get(self.live_server_url + '/recent-bills/')
        bills_text = self.browser.find_element_by_css_selector("#bills").text
        self.assertIn("Bill", bills_text)
        self.assertIn("Status", bills_text)
        self.assertIn("Sponsor", bills_text)

    def test_has_about_page(self):
        self.browser.get(self.live_server_url)
        navbar_text = self.browser.find_element_by_css_selector('.navbar').text
        self.assertIn("About", navbar_text)
        self.browser.get(self.live_server_url + '/about/')
        about_text = self.browser.find_element_by_css_selector('.about').text
        self.assertIn("This application was made possible by:", about_text)
        self.assertIn("Open Secrets API", about_text)
        self.assertIn("Propublica Congress API", about_text)
        self.assertIn("Sunlight Congress API", about_text)
        self.assertIn("GovTrack.us API", about_text)
