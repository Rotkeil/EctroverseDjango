# Generated by Django 3.1 on 2021-01-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201230_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='current_position_x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='fleet',
            name='current_position_y',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='fleet',
            name='i',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='command_order',
            field=models.IntegerField(choices=[(0, 'Attack Planet'), (1, 'Station On Planet'), (2, 'Move To System'), (3, 'Merge In System'), (4, 'Merge In System A'), (5, 'Join Main Fleet')], default=0),
        ),
    ]