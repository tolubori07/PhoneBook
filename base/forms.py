from django import forms
from.models import User,Contacts
from django.contrib.auth.forms import UserCreationForm
class Myusercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','address','sociallinks','phone_number']
        

class contactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['avatar','first_name','last_name','phone_number','email','address','sociallinks','favourites','Emergency']