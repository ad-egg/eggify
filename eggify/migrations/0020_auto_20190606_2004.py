# Generated by Django 2.2.2 on 2019-06-06 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0019_auto_20190606_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 6, 20, 4, 17, 916876, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='7ab0768b-edd0-4ec5-89f7-21fdbc039068', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
