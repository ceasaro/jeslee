from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

__author__ = 'ceasaro'


class Address(models.Model):

    class Meta:
        abstract = True

    street = models.CharField(_(u'street'), blank=True, max_length=100)
    street_nr = models.CharField(_(u'street number'), blank=True, max_length=10)
    zip = models.CharField(_(u'zip'), blank=True, max_length=100)
    city = models.CharField(_(u'city'), blank=True, max_length=100)
    country = models.CharField(_(u'country'), blank=True, max_length=100, default='Netherlands')

    def __repr__(self):
        return "Address[{pk}] {{{zip}, {street_nr}}}".format(pk=self.pk, zip=self.zip, street_nr=self.street_nr)


class Registration(TimeStampedModel, Address):

    class Meta:
        abstract = True

    name = models.CharField(_(u'name'), max_length=50)
    birth_date = models.DateField(_(u'birth date'), blank=True, max_length=10)
    email = models.CharField(_(u'email'), max_length=100)

    def __repr__(self):
        return "Registration[{pk}] {{{name}, {email}}}".format(pk=self.pk, name=self.name, email=self.email)


class ClothingSize(models.Model):
    size = models.CharField(u"clothing size", max_length=100)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "ClothingSize[{pk}] {{{size}}}".format(pk=self.pk, size=self.size)


class Garment(models.Model):
    name = models.CharField(_(u'name'), max_length=100)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Garment[{pk}] {{{name}}}".format(pk=self.pk, name=self.name)