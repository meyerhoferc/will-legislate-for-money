from django import template
from django.template.defaulttags import register
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
