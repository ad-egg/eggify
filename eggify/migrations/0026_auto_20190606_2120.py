# Generated by Django 2.2.2 on 2019-06-06 21:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0025_auto_20190606_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='006c85f0-a487-429e-b789-64c2f60f1c16', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 6, 21, 20, 57, 418869, tzinfo=utc), verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='words',
            field=models.TextField(help_text='Enter text to be eggified!'),
        ),
    ]