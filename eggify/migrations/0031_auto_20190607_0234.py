# Generated by Django 2.2.2 on 2019-06-07 02:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0030_auto_20190607_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='024b43f5-a332-4be9-aa09-7c8afd28f097', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 2, 34, 45, 392274, tzinfo=utc), verbose_name='updated at'),
        ),
    ]
