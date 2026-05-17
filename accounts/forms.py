from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Parol',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Parolni takrorlang',widget=forms.PasswordInput)

    def clean_confirm_password(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError('Parollar bir xil emas')
        return data['confirm_password']

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']