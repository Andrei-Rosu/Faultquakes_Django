# Generated by Django 2.1.2 on 2018-11-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faultquakes', '0014_auto_20181028_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, default='Journal', max_length=250),
        ),
    ]
