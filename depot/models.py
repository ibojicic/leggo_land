from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from hurry.filesize import size


class FFUnitsChoices(models.TextChoices):
    JY_BEAM = 'jy_beam', _('Jy per beam')


class FFUpload(models.Model):
    file_upload = models.FileField(upload_to='uploads', null=False, blank=False, default='')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    timestamp = models.DateField(auto_now_add=True, null=True, blank=True)
    telescope = models.CharField(max_length=255, )
    description = models.TextField()
    file_size = models.FloatField(null=True)
    parsed_header = models.JSONField(null=True)
    file_hash = models.CharField(max_length=43, null=True, unique=True)

    def human_file_size(self):
        return size(self.file_size)

    def __str__(self):
        return self.file_upload.name


class FF(models.Model):
    file_upload = models.ForeignKey(FFUpload, on_delete=models.SET_NULL, null=True)
    fits = models.FileField(upload_to='working', null=False, blank=False, default='')
    name = models.CharField(max_length=45, null=True, unique=True)
    frequency = models.FloatField(null=True)
    units = models.CharField(max_length=25, choices=FFUnitsChoices.choices, null=True)
    naxis3 = models.IntegerField(null=True)
    naxis4 = models.IntegerField(null=True)
    active = models.BooleanField(default=False)
    footprint = ArrayField(ArrayField(models.FloatField()), null=True)
    center_x = models.FloatField(null=True)
    center_y = models.FloatField(null=True)
    radius = models.FloatField(null=True)

    def __str__(self):
        return self.fits.name


class FFHeader(models.Model):
    fits = models.ForeignKey(FF, on_delete=models.CASCADE)
    parsed_header = models.JSONField()
    full_header = models.TextField()

    def __str__(self):
        return self.fits.fits.name



# class FFFootprint(models.Model):
#     fits = models.ForeignKey(FF, on_delete=models.CASCADE)
#     x0 = models.FloatField()
#     y0 = models.FloatField()
#     x1 = models.FloatField()
#     y1 = models.FloatField()
#     x2 = models.FloatField()
#     y2 = models.FloatField()
#     x3 = models.FloatField()
#     y3 = models.FloatField()
#
#     def __str__(self):
#         return self.fits.fits.name
