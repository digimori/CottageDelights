from django import forms
from .models import OrderRecord


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderRecord
        fields = ('full_name', 'email', 'mobile_number',
                  'home_number', 'house_name',
                  'address_line_1', 'address_line_2', 'town_city',
                  'postcode', 'country', 'county')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'home_number': 'Home Number',
            'mobile_number': 'Mobile Number',
            'house_name': 'House Name',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'town_city': 'Town or City',
            'county': 'County or State',
            'postcode': 'Postcode/Zip Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
