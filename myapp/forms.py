from django import forms

class myform(forms.Form):
    fname = forms.CharField()
    phone = forms.IntegerField()
