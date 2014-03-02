from datetime import date
from django.conf import settings
from django.db.models import Manager
from django.utils import formats
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel
from jeslee_web.base.models import Registration, Address, ClothingSize, Garment


class FashionRegistration(Registration):
    age = models.CharField(_(u'age'), null=True, max_length=5)
    fashion_show = models.CharField(u'fashion show', max_length=100)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "FashionRegistration[{pk}] {{{name}, {email}}}".format(pk=self.pk, name=self.name, email=self.email)


class FashionGarment(TimeStampedModel):
    garment = models.ForeignKey(Garment, related_name=u'garment')
    size = models.ForeignKey(ClothingSize)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "FashionGarment[{pk}] {{{name}, {size}}}".format(pk=self.pk, name=self.garment.name, size=self.size)


class FashionModel(TimeStampedModel, Address):
    name = models.CharField(_(u'name'), max_length=50)
    size = models.ForeignKey(ClothingSize, related_name=u'model', blank=True, null=True)
    garment = models.ForeignKey(FashionGarment, related_name=u'model', blank=True, null=True)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "FashionModel[{pk}] {{{name}, {size}}}".format(pk=self.pk, name=self.name, size=self.size)


class TicketOrder(TimeStampedModel):
    order_url = models.URLField(_(u'order url'))


class FashionLocation(TimeStampedModel, Address):
    name = models.CharField(_(u'name'), max_length=50)
    logo = models.FileField(upload_to='fashion_show/location/logos', blank=True, null=True)
    website = models.URLField(_(u'website'), blank=True, null=True)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "FashionLocation[{pk}] {{{name}}}".format(pk=self.pk, name=self.name)


class FashionShowManager(Manager):

    def get_upcoming_shows(self):
        """
        Returns all upcoming fashion shows ordered
        """
        today = date.today()
        return self.get_query_set().filter(start_time__gte=today)

    def get_upcoming_show(self):
        """
        Returns the next upcoming fashion show
        """
        qs = self.get_upcoming_shows()
        shows = list(qs[:1])
        if shows:
            return shows[0]
        return None


class FashionShow(TimeStampedModel):
    location = models.ForeignKey(FashionLocation, related_name=u'fashion_show')
    start_time = models.DateTimeField(_(u'start_time'), blank=True, null=True)
    end_time = models.DateTimeField(_(u'end_time'), blank=True, null=True)
    ticket_order = models.ForeignKey(TicketOrder, related_name=u'fashion_show', blank=True, null=True)
    models = models.ManyToManyField(FashionModel, related_name=u'fashion_shows', blank=True, null=True)

    objects = FashionShowManager()

    class Meta:
        ordering = ["start_time"]

    @property
    def start_date_f(self):
        return formats.date_format(self.start_time, "DATE_FORMAT")

    @property
    def start_time_f(self):
        return formats.time_format(self.start_time, "TIME_FORMAT")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "FashionShow[{pk}] {{{location}}}".format(pk=self.pk, location=self.location)

