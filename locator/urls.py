from django.urls import path

from .views import *

urlpatterns = [
    path('footprint-search/', FootprintSearchFormView.as_view(), name='footprint_search'),
]
