from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
