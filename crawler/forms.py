from django import forms
class CustomForm(forms.Form):
    City=forms.CharField(max_length=30,required=True,)
