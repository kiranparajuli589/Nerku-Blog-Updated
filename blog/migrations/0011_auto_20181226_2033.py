# Generated by Django 2.1.4 on 2018-12-26 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181226_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 14, 48, 37, 145359, tzinfo=utc)),
        ),
    ]