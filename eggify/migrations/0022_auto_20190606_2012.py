# Generated by Django 2.2.2 on 2019-06-06 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0021_auto_20190606_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='78304286-8ee1-4b81-9ee4-8378e5d3ef18', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 6, 20, 12, 8, 392421, tzinfo=utc), verbose_name='updated at'),
        ),
    ]