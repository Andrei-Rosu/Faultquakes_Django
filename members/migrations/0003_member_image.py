# Generated by Django 2.1.2 on 2018-11-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20181121_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='members_pics'),
        ),
    ]