# Generated by Django 2.2.2 on 2019-06-08 07:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0049_auto_20190608_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 7, 2, 17, 760145, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='8ff2c499-6d1d-4c5a-abba-3942baaa523c', editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]