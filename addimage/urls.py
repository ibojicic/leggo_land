from django.urls import path
from .views import *

urlpatterns = [
    path('add-image', AddImageView.as_view(), name='add_image'),
]
