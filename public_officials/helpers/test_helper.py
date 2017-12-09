from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from public_officials.views import *
from public_officials.models import *
from django.contrib.auth.models import User
from unittest import skip
import vcr

# class TestHelper():
#
#     # @class_method
#     def create_legislators(self, num):
#         num
#         # use FactoryBoy
#         Legislator.objects.create(first_name="Diana",
#                                   last_name="DeGette",
#                                   phone="12345",
#                                   email="email@email.com",
#                                   pid="D000197",
#                                   chamber="house",
#                                   party="D",
#                                   state="CO",
#                                   cid="N00006134")
