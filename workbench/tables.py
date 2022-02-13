import django_tables2 as tables

from depot.models import FFUpload, FF


##################################
##### Draft Applications Table ###
##################################

class FitsTable(tables.Table):

    # file_upload = tables.FileColumn()

    # fits = models.FileField(upload_to='working', null=False, blank=False, default='')
    # parsed_header = models.JSONField()

    class Meta:
        model = FF

        orderable = False

        attrs = {"id": "workbench", "class": "table table-bordered table-striped dataTable dtr-inline", }

        sequence = ( 'name', 'frequency', 'units')

        fields = ( 'name', 'frequency', 'units')

        template_name = "django_tables2/bootstrap.html"

##################################
## end Draft Applications Table ##
##################################
