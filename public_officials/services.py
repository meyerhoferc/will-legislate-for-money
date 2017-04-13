from django.http import HttpRequest, HttpResponse
import requests
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
