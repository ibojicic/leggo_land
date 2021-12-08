from django.db import models

# Create your models here.

class FitsFileUpload(models.Model):
    fits_file = models.FileField(upload_to='uploads', null=False, blank=False, default='')
    timestamp = models.DateField(auto_now_add=True, null=True, blank=True)