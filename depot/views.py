# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FitsFileUploadForm
from .models import FitsFileUpload


class SubmitFitsFileFormView(CreateView):
    model = FitsFileUpload
    template_name = 'depot/submit-fits-file-form-view.html'
    form_class = FitsFileUploadForm
    success_url = reverse_lazy('submit_fits_file_form_view')

    # def post(self, request, *args, **kwargs):
    #
    #     form_role = self.form_class(request.POST)
    #     print(request.POST)
    #     print(form_role)
    #
    #     if not form_role.is_valid():
    #         print(form_role.errors)
    #         return super().post(request, *args, **kwargs)
