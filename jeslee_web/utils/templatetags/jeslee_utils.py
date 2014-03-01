from django.conf import settings
from django.template.defaultfilters import stringfilter
from django import template
from datetime import datetime, date

__author__ = 'ceasaro'

register = template.Library()


@register.filter
@stringfilter
def get_age(birth_date_str, arg=None):
    """Returns the age of the given birth date."""
    if birth_date_str in (None, ''):
        return ''
    if arg is None:
        arg = settings.STRING_TO_DATE_FORMAT
    try:
        birth_date = datetime.strptime(birth_date_str, arg)
        today = datetime.today()
        try:
            birthday = birth_date.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = birth_date.replace(year=today.year, day=birth_date.day-1)
        if birthday > today:
            return today.year - birth_date.year - 1
        else:
            return today.year - birth_date.year
    except ValueError as er:
        return er
