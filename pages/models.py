from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.EmailField(verbose_name=_('name')),
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class BannerModel(models.Model):
    collection = models.CharField(max_length=60, verbose_name=_('collection'))
    title = models.CharField(max_length=60, verbose_name=_('title'))
    image = models.ImageField(upload_to='banners/', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    is_active = models.BooleanField(default=False, blank=True, verbose_name=_('is active'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

