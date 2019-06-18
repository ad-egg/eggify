# Generated by Django 2.2.2 on 2019-06-18 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0051_auto_20190608_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='eggnt',
            name='language',
            field=models.CharField(choices=[('EN', 'English')], default='EN', max_length=2),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 2, 3, 10, 91756, tzinfo=utc), editable=False, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='eggnt',
            name='id',
            field=models.CharField(default='2b821be9-a02e-4ab6-adf0-e35d88920f26', editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]