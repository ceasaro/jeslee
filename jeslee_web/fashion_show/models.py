from datetime import date
from django.conf import settings
from django.db.models import Manager
from django.utils import formats
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel
from jeslee_web.base.models import Registration, Address, ClothingSize, Garment, Location


class FashionGarment(TimeStampedModel):
    garment = models.ForeignKey(Garment, related_name=u'garment')
    size = models.ForeignKey(ClothingSize)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return u"FashionGarment[{pk}] {{{name}, {size}}}".format(pk=self.pk, name=self.garment.name, size=self.size)


class FashionModel(TimeStampedModel, Address):
    name = models.CharField(_(u'name'), max_length=50)
    size = models.ForeignKey(ClothingSize, related_name=u'model', blank=True, null=True)
    garment = models.ForeignKey(FashionGarment, related_name=u'model', blank=True, null=True)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return u"FashionModel[{pk}] {{{name}, {size}}}".format(pk=self.pk, name=self.name, size=self.size)


class FashionLocation(TimeStampedModel, Address, Location):
    name = models.CharField(_(u'name'), max_length=50)
    logo = models.FileField(upload_to='fashion_show/location/logos', blank=True, null=True)
    website = models.URLField(_(u'website'), blank=True, null=True)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return u"FashionLocation[{pk}] {{{name}}}".format(pk=self.pk, name=self.name)


class FashionShowManager(Manager):

    def get_upcoming_shows(self, date_from=date.today()):
        """
        Returns all upcoming fashion shows ordered
        """
        return self.get_query_set().filter(cancelled=False).filter(start_time__gte=date_from)

    def get_upcoming_show(self, date_from=date.today()):
        """
        Returns the next upcoming fashion show
        """
        qs = self.get_upcoming_shows(date_from)
        shows = list(qs[:1])
        if shows:
            return shows[0]
        return None


class FashionShow(TimeStampedModel):
    location = models.ForeignKey(FashionLocation, related_name=u'fashion_show')
    start_time = models.DateTimeField(_(u'start time'), blank=True, null=True)
    end_time = models.DateTimeField(_(u'end time'), blank=True, null=True)
    ticket_order_url = models.URLField(_(u'ticket order url'), blank=True, null=True)
    participate = models.BooleanField(_(u'participate'), default=True)
    cancelled = models.BooleanField(_(u'cancelled'), default=False)
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

    def __unicode__(self):
        start_time_strftime = self.start_time.strftime(settings.STRING_TO_DATE_FORMAT).lstrip('0')
        return _(u"{start_time}, {location} in {place}").format(start_time=start_time_strftime,
                                                          location=self.location.name,
                                                          place=self.location.city)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return u"FashionShow[{pk}] {{{location}}}".format(pk=self.pk, location=self.location)


class FashionRegistration(Registration):
    age = models.CharField(_(u'age'), null=True, max_length=5, error_messages={'required': 'Enter a valid phone number'})
    # fashion_show = models.CharField(_(u'fashion show'), max_length=100)
    fashion_show = models.ForeignKey(FashionShow, null=True, blank=True)
    remarks = models.TextField(_(u'remarks'), null=True, blank=True)
    size = models.ForeignKey(ClothingSize, null=True, blank=True)

    def __unicode__(self):
        return u"{name}, {email}".format(pk=self.pk, name=self.name, email=self.email)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return u"FashionRegistration[{pk}] {{{name}, {email}}}".format(pk=self.pk, name=self.name, email=self.email)
