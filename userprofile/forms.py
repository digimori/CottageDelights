from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated
        labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_home_number': 'Home Number',
            'default_mobile_number': 'Mobile Number',
            'default_house_name': 'House Name',
            'default_postcode': 'Postal Code',
            'default_town_city': 'Town or City',
            'default_address_line_1': 'Address Line 1',
            'default_address_line_2': 'Address Line 2',
            'default_county': 'County or State',
        }

        self.fields['default_home_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
