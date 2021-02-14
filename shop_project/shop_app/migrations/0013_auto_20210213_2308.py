# Generated by Django 3.1.2 on 2021-02-13 22:08

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productname',
            name='product_picture_2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='productname',
            name='product_picture_3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='productname',
            name='product_picture_4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='productname',
            name='product_picture_5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='productname',
            name='product_picture_6',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='pictures'),
        ),
    ]