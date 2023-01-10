from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .forms import ContactModelForm


class HomePageView(TemplateView):
    template_name = 'index.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')
