from django.contrib.auth.models import User
from django.db import models
from django.db.models import Manager
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel

from jeslee_web.base.models import Address


__author__ = 'ceasaro'


class ClientManager(Manager):
    """
    return all viewable clients
    """
    def viewable(self):
        return self.get_query_set().all()


class Client(TimeStampedModel, Address):
    name = models.CharField(_('name'), max_length=128, unique=True)
    user = models.ForeignKey(User, verbose_name=_(u"user"), blank=False, null=False)
    objects = ClientManager()

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class CategoryManager(Manager):

    def viewable(self):
        """
        return viewable categories
        """
        return self.get_query_set().all()


class Category(TimeStampedModel):
    name = models.CharField(_('name'), max_length=128)
    objects = CategoryManager()

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
