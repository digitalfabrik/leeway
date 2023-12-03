# Generated by Django 4.2.7 on 2023-12-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("leeway", "0008_leewaysimulation_traceback")]

    operations = [
        migrations.AddField(
            model_name="leewaysimulation",
            name="send_animation_sea",
            field=models.BooleanField(
                default=False,
                help_text="Attach Gif to e-mail with animation of particles with sea currents.",
            ),
        ),
        migrations.AddField(
            model_name="leewaysimulation",
            name="send_animation_wind",
            field=models.BooleanField(
                default=False,
                help_text="Attach Gif to e-mail with animation of particles and wind fields.",
            ),
        ),
        migrations.AddField(
            model_name="leewaysimulation",
            name="send_heatmap",
            field=models.BooleanField(
                default=False,
                help_text="Attach PNG to e-mail with heat map of final particle locations.",
            ),
        ),
        migrations.AddField(
            model_name="leewaysimulation",
            name="send_trajectories",
            field=models.BooleanField(
                default=True,
                help_text="Attach PNG to e-mail with particle trajectories.",
            ),
        ),
    ]
