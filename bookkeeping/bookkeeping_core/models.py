from django.contrib.auth.models import User
from django.db import models
from django.db.models import Manager
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel

from jeslee_web.base.models import Address


__author__ = 'ceasaro'


class Client(TimeStampedModel, Address):
    name = models.CharField(_('name'), max_length=128, unique=True)
    user = models.ForeignKey(User, verbose_name=_(u"user"), blank=False, null=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class CategoryManager(Manager):

    def viewable(self):
        """
        return all payments of given year, if year isn't specified return payments of current year
        """
        return self.get_query_set().all()

class Category(TimeStampedModel):
    name = models.CharField(_('name'), max_length=128)
    objects = CategoryManager()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
