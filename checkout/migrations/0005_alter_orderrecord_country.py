# Generated by Django 3.2 on 2023-05-11 14:30

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_rename_user_profile_orderrecord_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrecord',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
