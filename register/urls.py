from django.urls import path
from .views import MyRegistrationView

urlpatterns = [
    path('', MyRegistrationView.as_view(), name='register_registration'),

]