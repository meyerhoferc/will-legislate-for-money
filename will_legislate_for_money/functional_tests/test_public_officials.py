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
        self.browser.get(self.live_server_url)
        self.assertIn('Will Legislate For Money', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Your One Stop Corruption Watch', header_text)
        selection_text = self.browser.find_element_by_css_selector('.selections').text
        self.assertIn("View Senators", selection_text)
        self.assertIn("View Representatives", selection_text)
        self.assertIn("Search by State", selection_text)

    def test_checks_for_content_on_official_show(self):
        with vcr.use_cassette('cassettes/get_all_legislator_information'):
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
                                                   cid="N00006134")

            self.browser.get(self.live_server_url + '/legislators/%d/' % legislator.id)
            name_text = self.browser.find_element_by_tag_name('h1').text
            status_text = self.browser.find_element_by_tag_name('h5').text
            bio_text = self.browser.find_element_by_css_selector('.profile').text
            organization_text = self.browser.find_element_by_css_selector('.organization-contributors').text
            industry_text = self.browser.find_element_by_css_selector('.industry-contributors').text
            self.assertIn("Diana DeGette", name_text)
            self.assertIn("Colorado Representative", status_text)
            self.assertIn("Term: 2017-01-03 to 2019-01-03", bio_text)
            self.assertIn("Party: D", bio_text)
            self.assertIn("Email: email@email.com", bio_text)
            self.assertIn("Phone: 12345", bio_text)
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
