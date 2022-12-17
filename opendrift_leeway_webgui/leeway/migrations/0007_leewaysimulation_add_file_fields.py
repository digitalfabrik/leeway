# pylint: disable=invalid-name
# Generated by Django 4.1.4 on 2022-12-13 17:36

from django.db import migrations, models

import opendrift_leeway_webgui.leeway.models


class Migration(migrations.Migration):
    """
    Migration to add the file fields to the simulation model
    """

    dependencies = [("leeway", "0006_leewaysimulation_radius")]

    operations = [
        migrations.AddField(
            model_name="leewaysimulation",
            name="img",
            field=models.FileField(
                null=True,
                storage=opendrift_leeway_webgui.leeway.models.simulation_storage,
                upload_to="",
                verbose_name="Image file",
            ),
        ),
        migrations.AddField(
            model_name="leewaysimulation",
            name="netcdf",
            field=models.FileField(
                null=True,
                storage=opendrift_leeway_webgui.leeway.models.simulation_storage,
                upload_to="",
                verbose_name="NetCDF file",
            ),
        ),
    ]