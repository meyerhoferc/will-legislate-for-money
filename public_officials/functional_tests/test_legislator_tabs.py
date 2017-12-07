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

    def test_checks_for_profile_content_on_official_show(self):
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
            follow_button_text = self.browser.find_element_by_css_selector('#follow-legislator').text
            bio_text = self.browser.find_element_by_css_selector('.profile').text
            stats_text = self.browser.find_element_by_css_selector('.stats').text
            button_text = self.browser.find_element_by_css_selector('#follow-legislator').text
            self.assertNotIn('Follow', button_text)
            self.assertIn("Diana DeGette", name_text)
            self.assertNotIn("Follow", follow_button_text)
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

    def test_information_in_organization_text(self):
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
            self.browser.find_element_by_css_selector('#org-tab').click()
            organization_contributions_text = self.browser.find_element_by_css_selector('.organization-contributors').text
            self.assertIn('Contributions by Organization', organization_contributions_text)
            self.assertIn('Organization', organization_contributions_text)
            self.assertIn('Total', organization_contributions_text)
            self.assertIn('Individual Donations', organization_contributions_text)
            self.assertIn('PACs', organization_contributions_text)

    def test_information_in_industry_text(self):
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
            self.browser.find_element_by_css_selector('#ind-tab').click()
            industry_contributions_text = self.browser.find_element_by_css_selector('.industry-contributors').text
            self.assertIn('Contributions by Industry', industry_contributions_text)
            self.assertIn('Industry', industry_contributions_text)
            self.assertIn('Total', industry_contributions_text)
            self.assertIn('Individual Donations', industry_contributions_text)
            self.assertIn('PACs', industry_contributions_text)

    def test_information_in_sponsored_bills_text(self):
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
            self.browser.find_element_by_css_selector('#bill-tab').click()
            sponsored_bills_text = self.browser.find_element_by_css_selector('.sponsored-bills').text
            self.assertIn('Sponsored Bills', sponsored_bills_text)
            self.assertIn('Bill Title', sponsored_bills_text)
            self.assertIn('Introduction Date', sponsored_bills_text)

    def test_information_in_voting_history_text(self):
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
            self.browser.find_element_by_css_selector('#vote-tab').click()
            voting_history_text = self.browser.find_element_by_css_selector('.voting-history').text
            self.assertIn('Voting History', voting_history_text)
            self.assertIn('Proposition', voting_history_text)
            self.assertIn('Vote', voting_history_text)
            self.assertIn('Result', voting_history_text)
