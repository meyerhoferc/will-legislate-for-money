from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from public_officials.services import *

class LegislatorDataTest(TestCase):
    
    def test_service_gets_legislator_information(self):
        self.assertEqual(Legislator.objects.count(), 0)
        legislators = legislator_service.get_legislators
        self.assertEqual(Legislator.objects.count(), 10)
        legislator = Legislator.objects.first()
        self.assertTrue(legislator.name)
        self.assertTrue(legislator.state)
        self.assertTrue(legislator.cid)
