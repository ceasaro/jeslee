from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Registration(TimeStampedModel):
    
    class Meta:
        abstract = True

    name = models.CharField(u'name', max_length=50)
    birth_date = models.DateField(u'birth date', max_length=10)
    email = models.CharField(u'email', max_length=100)
    street = models.CharField(u'street', max_length=100)
    street_nr = models.CharField(u'street number', max_length=10)
    zip = models.CharField(u'zip', max_length=100)
    city = models.CharField(u'city', max_length=100)
    country = models.CharField(u'country', max_length=100, default='Netherlands')


class FashionRegistration(Registration):
    fashion_show = models.CharField(u'fashion show', max_length=100)