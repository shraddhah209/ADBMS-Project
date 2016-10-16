from django import forms

class SelectCOperRange(forms.Form):
    rangemin = forms.DecimalField(min_value=0, max_value=99, label='Enter minimum percentage')
    rangemax = forms.DecimalField(min_value=1, max_value=100, label='Enter maximum percentage')
