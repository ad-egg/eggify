# Generated by Django 2.0.13 on 2019-06-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eggify', '0005_auto_20190604_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggnt',
            name='created_at',
            field=models.DateTimeField(editable=False, verbose_name='created at'),
        ),
    ]
