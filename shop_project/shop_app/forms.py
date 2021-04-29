from django import forms
from . models import Buyer, ProductName


class BuyerForm(forms.ModelForm):
    address = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows':'2', 'cols': '50'}))
    class Meta:
        model = Buyer
        fields = '__all__'

        labels = {
            'buyed_item':'Odaberi Artikl',
        	'first_name':'Ime',
        	'last_name':'Prezime',
        	'email':'Imejl',
        	'phone':'Telefon',
        	'address':'Adresa',
        	'note':'Napomena',
        	}


class ProductNameForm(forms.ModelForm):
	class Meta:
		model = ProductName
		fields = (
			'user', 
			'product_brand', 
			'product_name', 
			'product_description', 
			'ad_image', 
			'product_picture_1', 
			'product_picture_2', 
			'product_picture_3', 
			'product_picture_4', 
			'product_picture_5', 
			'product_picture_6', 
			'product_price', 
			'phone'
			)

		widgets = {
			'user':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
		}


		# labels = {
		# 		'product_brand':'Brend',
		# 		'product_name':'Artikl',
		# 		'product_description':'Opis',
		# 		'ad_image':'Naslovna slika',
		# 		'product_picture_1':'Slika Artikla 1',
		# 		'product_picture_2':'Slika Artikla 2',
		# 		'product_picture_3':'Slika Artikla 3',
		# 		'product_picture_4':'Slika Artikla 4',
		# 		'product_picture_5':'Slika Artikla 5',
		# 		'product_picture_6':'Slika Artikla 6',
		# 		'product_price':'Cena Artikla',
		# 		'phone':'Telefon'
		# 		}