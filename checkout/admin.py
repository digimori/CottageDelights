from django.contrib import admin
from .models import OrderRecord, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'shopping_cart')

    fields = ('order_number', 'date', 'full_name',
              'email', 'mobile_number', 'home_number', 'country',
              'postcode', 'towncity', 'address_line_1',
              'address_line_2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'shopping_cart')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(OrderRecord, OrderAdmin)
