# Generated by Django 2.2.2 on 2019-06-08 06:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0047_auto_20190608_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='50b7a185-cd8f-49cf-b839-4909f704c880', editable=False, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 6, 43, 32, 790317, tzinfo=utc), editable=False, verbose_name='updated at'),
        ),
    ]
