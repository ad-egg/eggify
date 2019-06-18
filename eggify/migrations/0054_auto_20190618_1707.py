# Generated by Django 2.2.2 on 2019-06-18 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0053_auto_20190618_0459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eggnt',
            old_name='language',
            new_name='input_language',
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 17, 7, 45, 412616, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='3569cf4c-47e5-425a-bed2-9676a20b8eb8', editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]
