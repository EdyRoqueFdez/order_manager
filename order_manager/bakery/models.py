from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseAbstract


# Create your models here.


class Decoration(BaseAbstract):
    name = models.CharField(verbose_name=_('Name'), max_length=15)

    class Meta:
        db_table = 'decoration'
        ordering = ['name']

    def __str__(self):
        return self.name


class Flavor(BaseAbstract):
    name = models.CharField(verbose_name=_('Name'), max_length=15)

    class Meta:
        db_table = 'flavor'
        ordering = ['name']

    def __str__(self):
        return self.name


class Stuffed(BaseAbstract):
    name = models.CharField(verbose_name=_('Name'), max_length=15)

    class Meta:
        db_table = 'stuffed'
        ordering = ['name']

    def __str__(self):
        return self.name


class Addition(BaseAbstract):
    name = models.CharField(verbose_name=_('Name'), max_length=15)

    class Meta:
        db_table = 'addition'
        ordering = ['name']

    def __str__(self):
        return self.name


class Doily(BaseAbstract):
    name = models.CharField(verbose_name=_('Name'), max_length=15)

    class Meta:
        db_table = 'doily'
        ordering = ['name']

    def __str__(self):
        return self.name
