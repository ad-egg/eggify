# Generated by Django 2.2.2 on 2019-06-07 02:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0028_auto_20190607_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='689506bd-9eb4-47ad-92c7-cf3a8d92c49a', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 2, 30, 28, 767233, tzinfo=utc), verbose_name='updated at'),
        ),
    ]