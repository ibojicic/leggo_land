# Create your views here.
from django.views.generic import ListView
from django_tables2 import SingleTableMixin

from depot.models import FF
from locator.filters import PositionFilter
from workbench.tables import FitsTable


class FootprintSearchFormView(SingleTableMixin, ListView):
    model = FF
    table_class = FitsTable
    template_name = 'locator/search-table-view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return PositionFilter(self.request.GET, queryset).qs
