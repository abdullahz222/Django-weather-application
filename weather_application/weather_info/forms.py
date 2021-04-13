from django import forms

class UserForm(forms.Form):
    fname= forms.CharField(max_length=100)
    lname= forms.CharField(max_length=100)