# Generated by Django 2.1.2 on 2018-11-21 20:49

from django.db import migrations, models
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='member',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='member',
            name='office',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='member',
            name='status',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Permanent', 'Permanent'), ('Postdoc', 'Postdoc'), ('Phd', 'Phd'), ('Visitor', 'Visitor'), ('Former', 'Former')], default='exit', max_length=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Geodesy', 'Geodesy'), ('Rock mechanics', 'Rock mechanics'), ('Modeling', 'Modeling')], default='exit', max_length=31),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='www',
            field=models.URLField(blank=True),
        ),
    ]
