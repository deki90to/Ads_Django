from django.db import models
import uuid


class Category(models.Model):
    category_name = models.CharField(max_length=100, help_text='Category name')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, help_text='Product name')
    # product_spec = models.TextField(max_length=5000, help_text='Product specs')
    brand_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='product_category')

    def __str__(self):
        return self.brand_name


class ProductName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=1000)
    product_brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey('Buyer', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Buyer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(max_length=500)
    note = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}'