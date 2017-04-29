from django import template
from django.template.defaulttags import register
from public_officials.models import *
import pdb

register = template.Library()

@register.filter
def get_value(dictionary, key):
    if key and type(dictionary) is dict:
        return dictionary.get(key)

@register.filter
def get_nested_value(dictionary, key):
    if key and type(dictionary) is dict:
        return dictionary['@attributes'][key]

@register.filter
def get_sponsor_url(bill):
    legislators = Legislator.objects.filter(pid=bill['sponsor']['bioguideid'])
    if legislators.count() == 1:
        legislator_id = legislators.first().id
        legislator_url = "/legislators/%s" % legislator_id
        return legislator_url

@register.filter
def get_sponsor_name(bill):
    legislator_first_name = bill['sponsor']['firstname']
    legislator_last_name = bill['sponsor']['lastname']
    legislator_full_name = legislator_first_name + " " + legislator_last_name
    return legislator_full_name
