from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter
def get_value(dictionary, key):
    if key:
        return dictionary.get(key)
