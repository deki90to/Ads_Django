from django.db import models
import uuid
from django.urls import reverse
from django_resized import ResizedImageField
from datetime import datetime
# from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100, help_text='Category name')

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category_name']


class Brand(models.Model):
    brand_name =        models.CharField(max_length=255, help_text='Product name')
    brand_category =    models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand_name

    def get_absolute_url(self):
        return reverse('brand')

    class Meta:
        ordering = ['brand_name']


class ProductName(models.Model):
    user =                  models.ForeignKey(User, on_delete=models.CASCADE)
    id =                    models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_name =          models.CharField(max_length=200)
    product_description =   models.TextField(max_length=500)
    date_posted =           models.DateTimeField(auto_now_add=True)
    ad_image =              ResizedImageField(size=[320,240], quality=100, upload_to='pictures', blank=True, null=True)
    product_picture_1 =     ResizedImageField(quality=100, upload_to='pictures', blank=True, null=True)
    product_picture_2 =     ResizedImageField(quality=100, upload_to='pictures', blank=True, null=True)
    product_picture_3 =     ResizedImageField(quality=100, upload_to='pictures', blank=True, null=True)
    product_picture_4 =     ResizedImageField(quality=100, upload_to='pictures', blank=True, null=True)
    product_picture_5 =     ResizedImageField(quality=100, upload_to='pictures', blank=True, null=True)
    product_picture_6 =     ResizedImageField(quality=100, upload_to='pictures', blank=True, null=True)
    product_price =         models.IntegerField(default='0', null=True, blank=False)
    phone =                 models.CharField(max_length=20)
    product_brand =         models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (f'{self.product_name}, {self.product_price}e, {self.user}')

    def get_absolute_url(self):
        return reverse('product')

    class Meta:
        ordering = ['-date_posted']


class Buyer(models.Model):
    first_name =    models.CharField(max_length=200)
    last_name =     models.CharField(max_length=200)
    email =         models.EmailField()
    phone =         models.CharField(max_length=20)
    address =       models.TextField(max_length=100)
    note =          models.TextField(max_length=300, blank=True, null=True)
    date_buyed =    models.DateTimeField(auto_now_add=True)
    buyed_item =    models.OneToOneField('ProductName', on_delete=models.SET_NULL, null=True, blank=False)
    
    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

    def get_absolute_url(self):
        return reverse('buyer')

    class Meta:
        ordering = ['-date_buyed']
