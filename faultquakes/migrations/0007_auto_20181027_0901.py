# Generated by Django 2.1.2 on 2018-10-27 09:01

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faultquakes', '0006_auto_20181027_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='team',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Geodesy', 'Geodesy'), ('Rock mechanics', 'Rock mechanics'), ('Modeling', 'Modeling')], max_length=31),
        ),
        migrations.AlterField(
            model_name='research',
            name='team',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Geodesy', 'Geodesy'), ('Rock mechanics', 'Rock mechanics'), ('Modeling', 'Modeling')], max_length=31),
        ),
    ]