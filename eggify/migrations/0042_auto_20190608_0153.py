# Generated by Django 2.2.2 on 2019-06-08 01:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0041_auto_20190608_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='f49895e3-e894-475b-a236-29d39bcbc0fc', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 1, 53, 28, 58312, tzinfo=utc), editable=False, verbose_name='updated at'),
        ),
    ]
