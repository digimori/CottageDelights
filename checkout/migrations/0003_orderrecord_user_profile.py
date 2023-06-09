# Generated by Django 3.2 on 2023-05-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('checkout', '0002_orderrecord_stripe_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrecord',
            name='user_profile',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='orders', to='userprofile.userprofile'),
        ),
    ]
