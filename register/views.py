from django.urls import reverse_lazy
from registration.backends.simple.views import RegistrationView
from register.forms import MainRegistrationForm


class MyRegistrationView(RegistrationView):
    form_class = MainRegistrationForm
    success_url = reverse_lazy('submit_fits_file_form_view')
