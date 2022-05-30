from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'  # ['','']
        # exclude = ['','']

        def clean_owner_email(self):
            owner_email = self.cleaned.data.get('owner_email')
            if 'gmail' in owner_email or 'hotmail' in owner_email or 'yahoo' in owner_email:
                raise forms.validationError('please enter an official email address')
            return owner_email


