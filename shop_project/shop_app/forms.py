from django import forms
from . models import Buyer, ProductName


class BuyerForm(forms.ModelForm):
    address = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows':'2', 'cols': '50'}))

    class Meta:
        model = Buyer
        fields = '__all__'


class ProductNameForm(forms.ModelForm):
	class Meta:
		model = ProductName
		fields = ('user', 'product_brand', 'product_name', 'product_description', 'product_picture', 'product_price', 'phone')

		widgets = {
			'user':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
		}