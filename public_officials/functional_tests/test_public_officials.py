from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from public_officials.models import *
import vcr
import os
import pdb

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
                                                   cid="N00006134",
                                                   twitter_id="RepDianaDeGette")

            self.browser.get(self.live_server_url + '/legislators/%d/' % legislator.id)
            name_text = self.browser.find_element_by_tag_name('h1').text
            status_text = self.browser.find_element_by_tag_name('h3').text
            bio_text = self.browser.find_element_by_css_selector('.profile').text
            stats_text = self.browser.find_element_by_css_selector('.stats').text
            self.assertIn("Diana DeGette", name_text)
            self.assertIn("Colorado Representative", status_text)
            self.assertIn("Term Start: January 03, 2017", stats_text)
            self.assertIn("Term End: January 03, 2019", stats_text)
            self.assertIn("Party: D", stats_text)
            self.assertIn("email@email.com", stats_text)
            self.assertIn("Phone: 12345", stats_text)
            self.assertIn("Twitter", stats_text)
            tabs_text = self.browser.find_element_by_css_selector('#tabs').text
            self.assertIn('About', tabs_text)
            self.assertIn('Industry Contributions', tabs_text)
            self.assertIn('Organization Contributions', tabs_text)
            self.assertIn('Sponsored Bills', tabs_text)
            self.assertIn('Recent Decisions', tabs_text)

    def test_checks_for_content_on_legislators_senators_index(self):
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

        self.browser.get(self.live_server_url + '/senators/')
        header_text = self.browser.find_element_by_tag_name('h1').text
        texas_senator = self.browser.find_element_by_css_selector('#Texas-senators').text
        colorado_senator = self.browser.find_element_by_css_selector('#Colorado-senators').text
        self.assertIn("All Senators", header_text)
        self.assertIn("Henry Schmojo", texas_senator)
        self.assertNotIn("Henry Schmojo", colorado_senator)
        self.assertIn("Love Fluff", colorado_senator)
        self.assertNotIn("Love Fluff", texas_senator)
        self.assertNotIn("Diana DeGette", texas_senator)
        self.assertNotIn("Diana DeGette", colorado_senator)

    def test_checks_for_content_on_legislators_representative_index(self):
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
                                                   chamber="house",
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

        self.browser.get(self.live_server_url + '/representatives/')
        header_text = self.browser.find_element_by_tag_name('h1').text
        colorado_rep = self.browser.find_element_by_css_selector('#Colorado-reps').text
        texas_rep = self.browser.find_element_by_css_selector('#Texas-reps').text
        self.assertIn("All Representatives", header_text)
        self.assertIn("Henry Schmojo", texas_rep)
        self.assertNotIn("Henry Schmojo", colorado_rep)
        self.assertIn("Diana DeGette", colorado_rep)
        self.assertNotIn("Diana DeGette", texas_rep)

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
