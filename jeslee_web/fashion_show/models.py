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
        return "FashionRegistration{{{pk}] {{{name}, {email}}}".format(pk=self.pk, name=self.name, email=self.email)


class FashionGarment(TimeStampedModel):
    # garment = models.ForeignKey(Garment)
    size = models.ForeignKey(ClothingSize)

    def __repr__(self):
        return "FashionGarment[{pk}] {{{name}, {size}}}".format(pk=self.pk, name=self.name, size=self.size)


class FashionModel(TimeStampedModel, Address):
    name = models.CharField(_(u'name'), max_length=50)
    size = models.ForeignKey(ClothingSize)
    garment = models.ForeignKey(FashionGarment)

    def __repr__(self):
        return "FashionModel[{pk}] {{{name}, {size}}}".format(pk=self.pk, name=self.name, size=self.size)


class FashionLocation(TimeStampedModel, Address):
    name = models.CharField(_(u'name'), max_length=50)
    # models = models.ManyToOneRel(FashionModel, related_name=_(u'location'))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "FashionLocation{{{pk}] {{{name}}}".format(pk=self.pk, name=self.name)
