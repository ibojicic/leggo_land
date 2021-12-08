from django.urls import path
from .views import *

urlpatterns = [
    path('submit-fits', SubmitFitsFileFormView.as_view(), name='submit_fits_file_form_view'),
]
