__author__ = 'ceasaro'
from django import template

register = template.Library()

@register.filter
def key_value(dictionary, key):
    return dictionary[key] if key in dictionary else None