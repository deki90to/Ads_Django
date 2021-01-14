from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from . models import Category, Brand
from django.shortcuts import render

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'

class BrandListView(generic.ListView):
    model = Brand
    template_name = 'brand_list.html'