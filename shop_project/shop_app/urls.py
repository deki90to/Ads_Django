from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('brand/', views.BrandListView.as_view(), name='brand'),
    path('product_name/', views.DeviceListView.as_view(), name='device'),
    path('buyer/', views.BuyerListView.as_view(), name='buyer'),

    path('category/createview/', views.CategoryCreateView.as_view(), name='category-createview'),
]