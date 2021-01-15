from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from . models import Category, Brand, ProductName, Buyer
from django.shortcuts import render

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'

class BrandListView(generic.ListView):
    model = Brand
    template_name = 'brand_list.html'

class DeviceListView(generic.ListView):
	model = ProductName
	template_name = 'productname_list.html'

class BuyerListView(generic.ListView):
    model = Buyer
    template_name = 'buyer_list.html'



class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'category_form.html'
    fields = '__all__'