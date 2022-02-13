# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django_tables2 import SingleTableMixin

from depot.models import FFUpload, FF
from .forms import CoordinateSearchForm
from .models import CoordinateSearch
from .tables import FitsTable


class WorkbenchTableView(SingleTableMixin, ListView):
    model = FF
    table_class = FitsTable
    template_name = 'workbench/workbench-table-view.html'


class WorkbenchCutoutsView(CreateView):
    model = CoordinateSearch
    template_name = 'workbench/cutouts-view.html'
    form_class = CoordinateSearchForm
    success_url = reverse_lazy('workbench_cutouts_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = FitsTable(FFUpload.objects.all())
        return context

    def post(self, request, *args, **kwargs):

        form_cutouts = self.form_class(request.POST)

        if not form_cutouts.is_valid():
            return super().post(request, *args, **kwargs)

        return super().post(request, *args, **kwargs)

