# Generated by Django 2.1.2 on 2018-11-22 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faultquakes', '0019_geodesy_modeling_rock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newswall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('video', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='news_pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
