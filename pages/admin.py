from django.contrib import admin
from .models import ContactModel, BannerModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'is_active']
    list_display_links = ['title', 'collection']
    search_fields = ['title', 'collection']
    list_filter = ['created_at']