# Generated by Django 2.1.2 on 2018-10-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faultquakes', '0011_auto_20181028_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='doi',
            field=models.CharField(blank=True, default='DOI', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='journal',
            field=models.CharField(blank=True, default='Journal', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(blank=True, default='Publisher', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, default='Url', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='research',
            name='doi',
            field=models.CharField(blank=True, default='DOI', max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='journal',
            field=models.CharField(blank=True, default='Journal', max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='publisher',
            field=models.CharField(blank=True, default='Publisher', max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='url',
            field=models.CharField(blank=True, default='Url', max_length=250),
        ),
        migrations.AddField(
            model_name='research',
            name='year',
            field=models.IntegerField(default=2018),
        ),
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.CharField(blank=True, default='Authors', max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, default='Title', max_length=250),
        ),
        migrations.AlterField(
            model_name='research',
            name='authors',
            field=models.CharField(blank=True, default='Authors', max_length=250),
        ),
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.CharField(blank=True, default='Title', max_length=250),
        ),
    ]
