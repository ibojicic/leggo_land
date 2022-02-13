from django.db import models
from django.utils.translation import gettext_lazy as _
import leggo_fits.fixers as leggo_fix

# Create your models here.

class CoordinateFrameChoices(models.TextChoices):
    ICRS = 'icrs', _('ICRS')
    FK5 = 'fk5', _('FK5')
    FK4 = 'fk4', _('FK4')
    Galactic = 'galactic', _('Galactic')


class InputUnitsChoices(models.TextChoices):
    HMSDMS = 'hmsdms', _('hmsdms')
    DEG = 'deg', _('deg')


class CoordinateSearch(models.Model):
    input_coordinates = models.CharField(max_length=120)
    input_frame = models.CharField(max_length=20, choices=CoordinateFrameChoices.choices,
                                   default=CoordinateFrameChoices.ICRS)
    input_units = models.CharField(max_length=10, choices=InputUnitsChoices.choices, default=InputUnitsChoices.HMSDMS)

    gal_b = models.FloatField(null=True, blank=True)
    gal_l = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.gal_b, self.gal_l = leggo_fix.parse_coordinates(self.input_coordinates, self.input_frame, self.input_units)
        super(CoordinateSearch, self).save(*args, **kwargs)

