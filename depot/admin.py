from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import FFUpload, FF, FFHeader

admin.site.register(FFUpload)
admin.site.register(FF)
admin.site.register(FFHeader)
