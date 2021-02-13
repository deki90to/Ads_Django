from django.contrib import admin
from . models import Category, Brand, Buyer, ProductName

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Buyer)

admin.site.register(ProductName)

class ProductName(admin.ModelAdmin):
    list_display = '__all__'

    def get_queryset(self, request):
        queryset = super(ProductName, self).get_queryset(request)
        queryset = queryset.order_by('date_posted')
