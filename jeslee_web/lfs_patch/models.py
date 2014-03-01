# django imports
from django.db import models

# lfs imports
from lfs.criteria.models import Criterion
from jeslee_web.base.models import ClothingSize


class ClothingCriterion(ClothingSize, Criterion):
    pass

