# Generated by Django 3.2 on 2023-05-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrecord',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]