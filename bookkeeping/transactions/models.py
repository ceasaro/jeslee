from datetime import date

from django.db import models
from django.db.models import Manager
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel


__author__ = 'ceasaro'


class Client(TimeStampedModel):
    name = models.CharField(_('name'), max_length=128, unique=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(_('name'), max_length=128)


class Transaction(TimeStampedModel):

    pay_date = models.DateField(_('payment date'), blank=False, null=False)
    amount = models.DecimalField(_('amount'), blank=False, null=False, decimal_places=2, max_digits=10)
    description = models.TextField(_('description'))
    client = models.ForeignKey(Client, related_name='transactions', blank=False, null=False)
    category = models.ForeignKey(Category, related_name='transactions', blank=True, null=True)
    tax_percentage = models.IntegerField(_('tax'))

    @property
    def tax(self):
        return self.amount * self.tax_percentage / 100


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



class Receipt(Transaction):
    pass