# Generated by Django 4.0 on 2022-02-13 05:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depot', '0004_remove_fffootprint_x0_remove_fffootprint_x1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fffootprint',
            name='footprint',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None),
        ),
    ]