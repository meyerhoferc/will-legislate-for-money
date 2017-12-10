from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
from django.contrib.auth.models import User
from unittest import skip
import vcr
from public_officials.tests.factories import *

class LegislatorRelationshipsTest(TestCase):
    @skip('come back')
    def test_legislator_has_many_to_many_relationship_with_users(self):
        legislator_one = LegislatorFactory.create()
        legislator_two = LegislatorFactory.create()
        user = User.objects.create(username='test')
        user2 = User.objects.create(username='test2')

        legislator_one.users.add(user)
        legislator_one.users.add(user2)
        legislator_two.users.add(user)

        self.assertEqual(legislator_one.users.count(), 2)
        self.assertEqual(legislator_two.users.count(), 1)
        self.assertEqual(user.legislator_set.all().count(), 2)
        self.assertEqual(user2.legislator_set.all().count(), 1)
        self.assertEqual(user2.legislator_set.all().first(), legislator_one)
