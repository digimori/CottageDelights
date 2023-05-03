# Generated by Django 3.2 on 2023-05-02 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_rename_category_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=50)),
                ('full_name', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=300)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('home_number', models.CharField(max_length=20)),
                ('house_name', models.CharField(blank=True, max_length=30, null=True)),
                ('address_line_1', models.CharField(max_length=80)),
                ('address_line_2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_city', models.CharField(max_length=40)),
                ('county', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=10)),
                ('shopping_cart', models.TextField(default='')),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.orderrecord')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]