from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message','name','email','subject'] 
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','slug','body','image','category','status']