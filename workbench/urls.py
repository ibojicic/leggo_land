from django.urls import path
from .views import *

urlpatterns = [
    path('table/', WorkbenchTableView.as_view(), name='workbench_table_view'),
    path('cutouts/', WorkbenchCutoutsView.as_view(), name='workbench_cutouts_view'),
]
