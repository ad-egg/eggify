# Generated by Django 2.2.2 on 2019-06-07 02:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0029_auto_20190607_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='9db066dd-a2d8-4341-8eb9-88aa890f7711', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 2, 33, 13, 34454, tzinfo=utc), verbose_name='updated at'),
        ),
    ]