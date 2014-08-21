from django.conf import settings

__author__ = 'ceasaro'


def company_context(request):
    """
    add company data to every template context
    """
    return {'COMPANY': settings.COMPANY}