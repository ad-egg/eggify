# Generated by Django 2.2.2 on 2019-06-05 02:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0015_auto_20190605_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 5, 2, 51, 21, 32208, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='uid',
            field=models.CharField(default='eb48197b-ff60-4411-9b80-03f989cc85cc', editable=False, max_length=50),
        ),
    ]