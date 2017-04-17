from django.http import HttpRequest, HttpResponse
import requests
import json
import pdb
from public_officials.models import Legislator
from will_legislate_for_money.secrets import *

class LegislatorService:
    def __init__(self):
        self.open_secrets_key = OPEN_SECRETS_KEY

    def get_legislators_by_state(self, state='CO'):
        url = "https://www.opensecrets.org/api/"
        payload = {
            'apikey': self.open_secrets_key,
            'output': 'json',
            'method': 'getLegislators',
            'id': state
            }
        legislators = requests.get(url, params=payload)
        legislators_json = legislators.json()['response']['legislator']
        all_legislators = []
        for legislator in legislators_json:
            legislator_data = legislator["@attributes"]
            legislator = Legislator.objects.create(name=legislator_data["firstlast"],
                                                   state=state,
                                                   cid=legislator_data["cid"])
            all_legislators.append(legislator)
        return all_legislators

    def get_legislator_profile(self, cid):
        url = "https://www.opensecrets.org/api/"
        payload = {
            'apikey': self.open_secrets_key,
            'output': 'json',
            'method': 'candSummary',
            'cid': cid
            }
        legislator_json = requests.get(url, params=payload)
        legislator = json.loads(legislator_json.content)['response']['summary']['@attributes']
        Legislator.objects.create(name=legislator['cand_name'],
                                  state=legislator['state'],
                                  cid=cid)
        return legislator

    def get_legislator_org_contributions(self, cid):
        url = "https://www.opensecrets.org/api/"
        payload = {
            'apikey': self.open_secrets_key,
            'output': 'json',
            'method': 'candContrib',
            'cid': cid
            }
        organizations_json = requests.get(url, params=payload)
        organizations = json.loads(organizations_json.content)['response']['contributors']['contributor']
        return organizations

    def get_legislator_ind_contributions(self, cid):
        url = "https://www.opensecrets.org/api/"
        payload = {
            'apikey': self.open_secrets_key,
            'output': 'json',
            'method': 'candIndustry',
            'cid': cid
            }
        industries_json = requests.get(url, params=payload)
        industries = json.loads(industries_json.content)['response']['industries']['industry']
        return industries

    def get_all_legislators(self):
        url = "https://congress.api.sunlightfoundation.com/legislators"
        payload = {
            'per_page': 'all'
        }
        legislators_json = requests.get(url, params=payload)
        legislators = json.loads(legislators_json.content)['results']
        return legislators
