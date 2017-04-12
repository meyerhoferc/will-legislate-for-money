from django.http import HttpRequest, HttpResponse
import requests
import pdb

class LegislatorService:
    def __init__(self, id='CO'):
        self.open_secrets_key = "dbb983c8877ccb8a95710d7bc4abc5a2"
        self.id = id

    def get_legislators(self):
        url = "https://www.opensecrets.org/api/"
        payload = {
            'apikey': self.open_secrets_key,
            'output': 'json',
            'method': 'getLegislators',
            'id': self.id
            }
        legislators = requests.get(url, params=payload)
        legislators_json = legislators.json()['response']['legislator']
        all_legislators = []
        for legislator in legislators_json:
            Legislator.objects.create()
        return all_legislators
