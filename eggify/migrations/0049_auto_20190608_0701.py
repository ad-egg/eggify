# Generated by Django 2.2.2 on 2019-06-08 07:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0048_auto_20190608_0643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eggnt',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='eggnt',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 7, 1, 23, 707651, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='a7eb274e-50b6-44be-8a54-e6f7fbc2dbc7', editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]
