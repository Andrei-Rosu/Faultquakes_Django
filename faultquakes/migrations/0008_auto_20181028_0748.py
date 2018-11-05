# Generated by Django 2.1.2 on 2018-10-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faultquakes', '0007_auto_20181027_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='content',
        ),
        migrations.RemoveField(
            model_name='research',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='doi',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='journal',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='doi',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='journal',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='publisher',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='url',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='research',
            name='authors',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.CharField(default=None, max_length=250),
        ),
    ]