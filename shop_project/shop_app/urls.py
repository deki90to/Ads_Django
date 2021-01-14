from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('brand/', views.BrandListView.as_view(), name='brand'),
]
