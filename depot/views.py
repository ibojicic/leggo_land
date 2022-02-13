# Create your views here.
import os

from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from leggo_fits import checkers
from leggo_fits.parsers import get_all_header_items, object_table_header
from .forms import FitsFileUploadForm, FitsDetailsForm
from .models import FFUpload, FF
from .tables import HeaderTable


class SubmitFitsFileFormView(CreateView):
    model = FFUpload
    template_name = 'depot/submit-fits-file-form-view.html'
    form_class = FitsFileUploadForm

    def post(self, request, *args, **kwargs):

        form_file_upload = self.form_class(request.POST, request.FILES)

        if not form_file_upload.is_valid():
            return super().post(request, *args, **kwargs)

        new_file = form_file_upload.save(commit=False)
        new_file.save()

        try:
            new_file.file_size = new_file.file_upload.size
            new_file.file_hash = checkers.get_hash(str(new_file.file_upload.path))
            new_file.user = request.user
            file_name = os.path.basename(str(new_file.file_upload))
            parsed_header, original_header = get_all_header_items(file_name)
            new_file.parsed_header = parsed_header
            new_file.save()
        except IntegrityError:
            new_file.delete()
            return super().post(request, *args, **kwargs)

        return HttpResponseRedirect(reverse('proccess_upload', kwargs={'pk': new_file.pk}))
        # return HttpResponseRedirect(reverse('fits_details_form_view',
        #                                     kwargs={'upfitspk': new_file.pk,
        #                                             'slice': 1}
        #                                     )
        #                             )


class FitsDetailsView(UpdateView):
    template_name = 'depot/fits-details-form-view.html'
    model = FF
    form_class = FitsDetailsForm
    file_upload = None

    # success_url = reverse_lazy('workbench_table_view')

    def get_success_url(self):
        inactive_fits = FF.objects.filter(id=self.file_upload.id, active=False)
        if inactive_fits.exists():
            return reverse('fits_details_form_view',
                           kwargs={'upfitspk': self.file_upload.id,
                                   'pk'      : inactive_fits.first().id}
                           )

        else:
            return reverse('workbench_table_view')

    def dispatch(self, request, *args, **kwargs):
        self.file_upload = FFUpload.objects.get(pk=self.kwargs.get('upfitspk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_upload'] = self.file_upload
        context['header_table'] = HeaderTable(object_table_header(self.file_upload.parsed_header))
        return context

    def form_valid(self, form):
        self.object.active = True
        self.object.save()
        return super().form_valid(form)
