# Generated by Django 3.2 on 2023-05-09 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderrecord_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderrecord',
            old_name='user_profile',
            new_name='userprofile',
        ),
    ]
