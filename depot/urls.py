from django.urls import path

from .utils import proccess_upload
from .views import *

urlpatterns = [
    path('submit-fits/', SubmitFitsFileFormView.as_view(), name='submit_fits_file_form_view'),
    path('fits-details/<int:upfitspk>/<int:pk>/', FitsDetailsView.as_view(), name='fits_details_form_view'),
    path('', SubmitFitsFileFormView.as_view(), name='submit_fits_file_form_view'),
    path('proccess-upload/<int:pk>/', proccess_upload, name='proccess_upload'),
]
