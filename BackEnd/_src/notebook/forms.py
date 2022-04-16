from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    last = forms.CharField(max_length=20)
    edad = forms.IntegerField(max_value=100)
