# Generated by Django 2.1.2 on 2018-10-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faultquakes', '0003_auto_20181022_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='team',
            field=models.CharField(choices=[('GEODESY', 'geodesy'), ('ROCK MECHANICS', 'rock mechanics'), ('MODELING', 'modeling')], default='exit', max_length=14),
            preserve_default=False,
        ),
    ]
