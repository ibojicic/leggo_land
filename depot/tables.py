import django_tables2 as tables


class HeaderTable(tables.Table):
    key = tables.Column()
    value = tables.Column()

    class Meta:
        orderable = False

        attrs = {"id": "headertable", "class": "table table-bordered table-striped dataTable dtr-inline", }

        sequence = ('key', 'value',)

        template_name = "django_tables2/bootstrap.html"
