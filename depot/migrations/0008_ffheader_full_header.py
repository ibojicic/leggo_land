# Generated by Django 4.0 on 2022-02-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depot', '0007_ff_center_x_ff_center_y_ff_radius_alter_ff_footprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='ffheader',
            name='full_header',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
