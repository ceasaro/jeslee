# django imports
from django.db import models

# lfs imports
from lfs.criteria.models import Criterion


class ClothingCriterion(models.Model, Criterion):
    CHILD_80 = '80'
    CHILD_86 = '86'
    CHILD_92 = '92'
    CHILD_98 = '98'
    CHILD_104 = '104'
    CHILD_110 = '110'
    CHILD_116 = '116'
    CHILD_122 = '122'
    CHILD_128 = '128'
    CHILD_134 = '134'
    CHILD_140 = '140'
    CHILD_146 = '146'
    CHILD_152 = '152'
    CHILD_158 = '158'
    CHILD_164 = '164'
    CHILD_176 = '176'
    CHILD_CLOTH_SIZES_CHOICES = (
        (CHILD_80, CHILD_80),
        (CHILD_86, CHILD_86),
        (CHILD_92, CHILD_92),
        (CHILD_98, CHILD_98),
        (CHILD_104, CHILD_104),
        (CHILD_110, CHILD_110),
        (CHILD_116, CHILD_116),
        (CHILD_122, CHILD_122),
        (CHILD_128, CHILD_128),
        (CHILD_134, CHILD_134),
        (CHILD_140, CHILD_140),
        (CHILD_146, CHILD_146),
        (CHILD_152, CHILD_152),
        (CHILD_158, CHILD_158),
        (CHILD_164, CHILD_164),
        (CHILD_176, CHILD_176),
        )
    size = models.CharField(u"size", max_length=100, choices=CHILD_CLOTH_SIZES_CHOICES)

