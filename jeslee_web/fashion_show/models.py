from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Registration(TimeStampedModel):
    
    class Meta:
        abstract = True

    name = models.CharField(_(u'name'), max_length=50)
    birth_date = models.DateField(_(u'birth date'), max_length=10)
    email = models.CharField(_(u'email'), max_length=100)
    street = models.CharField(_(u'street'), max_length=100)
    street_nr = models.CharField(_(u'street number'), max_length=10)
    zip = models.CharField(_(u'zip'), max_length=100)
    city = models.CharField(_(u'city'), max_length=100)
    country = models.CharField(_(u'country'), max_length=100, default='Netherlands')


class FashionRegistration(Registration):
    fashion_show = models.CharField(u'fashion show', max_length=100)