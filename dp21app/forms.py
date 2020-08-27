from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re

def vname(name):
    if len(name)>20:
        raise ValidationError("Name should be less than 20 characters")
    return name

class SampleForm(forms.Form):
    name=forms.CharField(max_length=30,required=True,label="Name :",
    validators=[vname])

    email=forms.EmailField(max_length=100,required=True,label="Email :",
    validators=[validators.MinLengthValidator(10)])

    cemail=forms.EmailField(max_length=100,required=True,label="Confirm Email :")

    ipadrs=forms.CharField(max_length=100,required=True,label="IP Address :",
    validators=[validators.validate_ipv4_address])

    pwd=forms.CharField(max_length=50,required=True,label="Password :",widget=forms.PasswordInput(attrs={'placeholder':"password"}))

    propic=forms.ImageField(required=True,label="Profile Picture :")

    botcatcher=forms.CharField(required=False,max_length=10,widget=forms.HiddenInput)

    def clean(self,*args,**kwargs):
        cleaned_data=super().clean() #getting all the data that is filled in the form
        email=cleaned_data.get("email")
        cemail=cleaned_data.get("cemail")
        if email==cemail:
            return cleaned_data
        self.add_error('cemail',"Both the emails are not same")
        self.add_error('email',"both the emails are not same please check")

    def clean_name(self):
        name=self.cleaned_data.get("name")
        for i in name:
            if not('a'<=i<='z' or 'A'<=i<='Z'):
                raise ValidationError("Name should only contain alphabets")
            return name
    
    def clean_botcatcher(self):
        bc=self.cleaned_data.get("botcatcher")
        if len(bc)==0:
            return bc
        self.add_error('name',"Hey robot you caught by the system")
        
