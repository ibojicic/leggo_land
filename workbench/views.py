# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from django_tables2 import SingleTableMixin

from depot.models import FFUpload, FF
from locator.filters import PositionFilter
from .forms import CoordinateSearchForm, CutoutForm
from .models import CoordinateSearch
from .tables import FitsTable


class WorkbenchTableView(SingleTableMixin, ListView):
    model = FF
    table_class = FitsTable
    template_name = 'workbench/workbench-table-view.html'


class WorkbenchCutoutsView(SingleTableMixin, FormView, ListView):
    model = FF
    table_class = FitsTable
    template_name = 'workbench/cutouts-view.html'
    form_class = CutoutForm

    def get_queryset(self):
        queryset = super(WorkbenchCutoutsView, self).get_queryset()
        return PositionFilter(self.request.GET, queryset).qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = FitsTable(FFUpload.objects.all())
        return context
    #
    # def post(self, request, *args, **kwargs):
    #
    #     form_cutouts = self.form_class(request.POST)
    #
    #     if not form_cutouts.is_valid():
    #         return super().post(request, *args, **kwargs)
    #
    #     return super().post(request, *args, **kwargs)
    #
