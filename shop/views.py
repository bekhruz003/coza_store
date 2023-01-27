from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductModel


class ShopView(ListView):
    template_name = 'product.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.all()

        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)
        return qs


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product-detail.html'
