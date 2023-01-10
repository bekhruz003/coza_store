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
