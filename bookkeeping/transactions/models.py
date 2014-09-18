from datetime import date

from django.db import models
from django.db.models import Manager
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel

from bookkeeping.bookkeeping_core.models import Client, Category


__author__ = 'ceasaro'


class Transaction(TimeStampedModel):

    pay_date = models.DateField(_('payment date'), blank=False, null=False)
    amount = models.DecimalField(_('amount'), blank=False, null=False, decimal_places=2, max_digits=10)
    description = models.TextField(_('description'))
    client = models.ForeignKey(Client, related_name='transactions', blank=False, null=False)
    category = models.ForeignKey(Category, related_name='transactions', blank=True, null=True)
    tax_percentage = models.IntegerField(_('btw percentage'), blank=True, null=True)
    tax = models.DecimalField(_('btw'), blank=False, null=False, decimal_places=2, max_digits=10)


class PaymentManager(Manager):

    def of_year(self, year=None):
        """
        return all payments of given year, if year isn't specified return payments of current year
        """
        if not year:
            year = date.today().year
        first_date_of_year = date(year, 1, 1)
        last_date_of_year = date(year, 12, 31)
        return self.get_query_set().filter(pay_date__range=(first_date_of_year, last_date_of_year))


class Payment(Transaction):
    objects = PaymentManager()

    class Meta:
        ordering = ['pay_date']


class Receipt(Transaction):
    pass