# Generated by Django 2.2.2 on 2019-06-06 20:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0022_auto_20190606_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='bf5a1f18-edfe-4129-9ce6-cc96d38867ed', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 6, 20, 13, 31, 600736, tzinfo=utc), verbose_name='updated at'),
        ),
    ]