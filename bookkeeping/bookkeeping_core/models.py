from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel

from jeslee_web.base.models import Address


__author__ = 'ceasaro'


class Client(TimeStampedModel, Address):
    name = models.CharField(_('name'), max_length=128, unique=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(_('name'), max_length=128)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
