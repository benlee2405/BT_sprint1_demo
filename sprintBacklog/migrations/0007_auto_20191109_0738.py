# Generated by Django 2.2.5 on 2019-11-09 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprintBacklog', '0006_remove_sprint_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2019, 11, 9), null=True),
        ),
    ]
