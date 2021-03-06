# Generated by Django 2.1.5 on 2020-02-29 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='summary',
            new_name='description',
        ),
        migrations.AddField(
            model_name='listing',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 29, 22, 6, 27, 35427)),
        ),
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
