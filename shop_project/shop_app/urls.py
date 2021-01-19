from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category'),
    path('brand/', views.BrandListView.as_view(), name='brand'),
    path('product_name/', views.DeviceListView.as_view(), name='product'),
    path('buyer/', views.BuyerListView.as_view(), name='buyer'),

    path('category/createview/', views.CategoryCreateView.as_view(), name='category-createview'),
    path('brand/createview/', views.BrandCreateView.as_view(), name='brand-createview'),
    path('productname/createview/', views.ProductNameCreateView.as_view(), name='productname-createview'),
    path('buyer/createview/', views.BuyerCreateView.as_view(), name='buyer-createview'),
]