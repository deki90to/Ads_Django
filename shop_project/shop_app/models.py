from django.db import models
import uuid
from django.urls import reverse
from django_resized import ResizedImageField
from datetime import datetime
# from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category_name = models.CharField(max_length=100, help_text='Category name')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category')


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, help_text='Product name')
    brand_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='product_category')

    def __str__(self):
        return self.brand_name

    def get_absolute_url(self):
        return reverse('brand')


class ProductName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    product_picture = ResizedImageField(size=[200,110], quality=100, upload_to='pictures', null=True, blank=True)
    product_brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    product_price = models.CharField(max_length=7, default='', null=True, blank=True)
    buyer = models.ForeignKey('Buyer', on_delete=models.SET_NULL, null=True, blank=True, related_name='buyer')

    def __str__(self):
        return (f'{self.product_name}, {self.product_price} (EU)')

    def get_absolute_url(self):
        return reverse('product')


class Buyer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(max_length=500)
    note = models.TextField(max_length=1000)
    date_buyed = models.DateTimeField(auto_now_add=True)
    # buyed = models.ForeignKey('ProductName', on_delete=models.SET_NULL, null=True, blank=True, related_name='buyed')


    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

    def get_absolute_url(self):
        return reverse('buyer')