# Generated by Django 2.1.2 on 2018-11-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faultquakes', '0016_auto_20181112_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
