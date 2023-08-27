

from django import forms

class DataFilterForm(forms.Form):
    field1 = forms.CharField(max_length=100, required=False)
    field2 = forms.IntegerField(required=False)

