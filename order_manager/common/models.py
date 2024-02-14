from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Currency(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=15)
    abbreviation = models.CharField(verbose_name=_('Abbreviation'), max_length=3)

    def __str__(self):
        return self.name


class BaseAbstract(models.Model):
    price = models.DecimalField(verbose_name=_('Price'), max_digits=15, decimal_places=2, default=0,
                                validators=[MinValueValidator(0)])
    currency = models.ForeignKey(Currency, verbose_name=_('Currency'), on_delete=models.PROTECT)

    class Meta:
        abstract = True
