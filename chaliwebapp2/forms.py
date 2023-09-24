from django import forms
from .models import User

class User(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phonenumber', 'email']

    def clean_phonenumber(self):
        phone_number = self.cleaned_data['phonenumber']
        # Validate phone number here
        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']
        # Validate email address here
        return email
