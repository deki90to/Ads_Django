from django import forms
from . models import Buyer

class BuyerForm(forms.ModelForm):
    address = forms.CharField(max_length=2000, 
    widget=forms.Textarea(attrs={'rows':'2', 'cols': '50'}))

    class Meta:
        model = Buyer
        fields = '__all__'