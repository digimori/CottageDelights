# Generated by Django 3.2 on 2023-06-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_orderrecord_house_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrecord',
            name='house_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
