# django imports
from datetime import date

# lfs imports
from lfs.criteria.models import Criterion
from jeslee_web.base.models import ClothingSize


class ClothingCriterion(ClothingSize, Criterion):
    pass

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# lfs imports
from lfs.plugins import OrderNumberGenerator as Base


class OrderNumberGenerator(Base):
    """
    Generates order numbers and saves the last one.

    **Attributes:**

    last
        The last stored/returned order number.

    format
        The format of the integer part of the order number.
    """
    last = models.IntegerField(_(u"Last order number"), default=2014)
    format = models.CharField(blank=True, max_length=20)

    def get_next(self, formatted=True):
        """Returns the next order number.

        **Parameters:**

        formatted
            If True the number will be returned within the stored format.
        """
        self.last += 1
        self.save()
        number_length = 5
        last_length = len(str(self.last))
        number_prefix = '0'*(number_length - last_length)
        prefixed_number = number_prefix + str(self.last)

        if formatted and self.format:
            formatted_id = self.format % prefixed_number
        else:
            formatted_id = '{year}-{number}'.format(year=date.today().year, number=prefixed_number)
        return formatted_id