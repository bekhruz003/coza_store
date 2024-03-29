import decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class ColorModel(models.Model):
    code = models.CharField(max_length=60, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    short_description = models.CharField(max_length=255, verbose_name=_('short description'))
    long_description = RichTextUploadingField(verbose_name=_('long description'))
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    main_image = models.ImageField(upload_to='products/', verbose_name=_('main image'))
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT, related_name='products',
                                 verbose_name=_('category'))
    tags = models.ManyToManyField(ProductTagModel,
                                  related_name='products',
                                  verbose_name=_('tags'))
    colors = models.ManyToManyField(ColorModel,
                                    related_name='products',
                                    verbose_name=_('colors'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def get_price(self):
        if self.discount:
            return ((100 - self.discount) / 100) * self.price
        return self.price

    def is_discount(self):
        return bool(self.discount)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
