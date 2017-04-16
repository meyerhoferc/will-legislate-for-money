from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from public_officials.models import *
import vcr
import pdb

class GuestUserTest(StaticLiveServerTestCase):
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

    def test_checks_for_content_on_official_show(self):
        with vcr.use_cassette('cassettes/get_all_legislator_information'):
            legislator = Legislator.objects.create(name="D",
                                                   state="CO",
                                                   cid="N00006134")
            self.browser.get(self.live_server_url + '/legislators/%d/' % legislator.id)
            name_text = self.browser.find_element_by_tag_name('h1').text
            status_text = self.browser.find_element_by_tag_name('h5').text
            bio_text = self.browser.find_element_by_css_selector('.profile').text
            organization_text = self.browser.find_element_by_css_selector('.organization-contributors').text
            industry_text = self.browser.find_element_by_css_selector('.industry-contributors').text
            self.assertIn("DeGette, Diana", name_text)
            self.assertIn("CO Representative", status_text)
            self.assertIn("First Elected: 1996", bio_text)
            self.assertIn("Next Election: 2016", bio_text)
            self.assertIn("Party: D", bio_text)
            self.assertIn("State: CO", bio_text)
            self.assertIn("Last Updated: 12/31/2016", bio_text)
            self.assertIn("PACs", organization_text)
            self.assertIn("Total", organization_text)
            self.assertIn("Individual Donations", organization_text)
            self.assertIn("Democracy Engine", organization_text)
            self.assertIn("$136825", organization_text)
            self.assertIn("$0", organization_text)
            self.assertIn("$136825", organization_text)
            self.assertIn("PACs", industry_text)
            self.assertIn("Total", industry_text)
            self.assertIn("Individual Donations", industry_text)
            self.assertIn("Pharmaceuticals/Health Products", industry_text)
            self.assertIn("$0", industry_text)
            self.assertIn("$144254", industry_text)
            self.assertIn("$144254", industry_text)
