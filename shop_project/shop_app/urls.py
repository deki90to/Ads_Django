from django.urls import path
from django.views.generic.base import View
from . import views


urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('brand/', views.BrandListView.as_view(), name='brand'),
    path('', views.product, name='product'),
    path('buyer/', views.BuyerListView.as_view(), name='buyer'),

    path('category/createview/', views.CategoryCreateView.as_view(), name='category-createview'),
    path('brand/createview/', views.BrandCreateView.as_view(), name='brand-createview'),
    path('productname/createview/', views.ProductNameCreateView.as_view(), name='productname-createview'),
    path('buyer/createview/', views.BuyerCreateView.as_view(), name='buyer-createview'),

    path('contact_list/', views.contact, name='contact_list'),

    path('<pk>/delete_item/', views.ProductNameDeleteView.as_view(), name='delete_item'),

    path('<pk>/update_item/', views.ProductNameUpdateView.as_view(), name='update_item'),
    path('<pk>/images/', views.ImagesDetailView.as_view(), name='images_detailview'),

    path('search/', views.search, name='search'),
]