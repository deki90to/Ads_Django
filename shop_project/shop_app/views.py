from django.db.models import fields
from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from . models import *
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from . forms import BuyerForm, ProductNameForm
from django.forms.models import model_to_dict



class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'

class BrandListView(generic.ListView):
    model = Brand
    template_name = 'brand_list.html'

def product(request):
    products = ProductName.objects.all()
    buyers = Buyer.objects.all()

    return render(request, 'productname_list.html', {'products': products, 'buyers': buyers})


class BuyerListView(generic.ListView):
    model = Buyer
    template_name = 'buyer_list.html'



class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'category_form.html'
    fields = '__all__'

class BrandCreateView(generic.CreateView):
    model = Brand
    template_name = 'brand_form.html'
    fields = '__all__'

class ProductNameCreateView(generic.CreateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'productname_form.html'
    # fields = ('user', 'product_brand', 'product_name', 'product_description', 'product_picture', 'product_price')
    ordering = ['-id']

class BuyerCreateView(generic.CreateView):
    model = Buyer
    template_name = 'buyer_form.html'
    # fields = '__all__'
    # ordering = ['-date_buyed']
    form_class = BuyerForm

def contact(request):
    return render(request, 'contact_list.html')



class ProductNameDeleteView(generic.DeleteView):
    model = ProductName
    template_name = 'delete_item.html'
    success_url = reverse_lazy('product')


class ProductNameUpdateView(generic.UpdateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'update_item.html'
    success_url = reverse_lazy('product')


class ImagesDetailView(generic.DetailView):
    model = ProductName
    template_name = 'images_details.html'


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        products = ProductName.objects.filter(product_brand__brand_name__icontains=search)

        context = {'search':search, 'products':products}
        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')