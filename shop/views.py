from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductModel, ProductTagModel, CategoryModel


class ShopView(ListView):
    template_name = 'product.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.all()

        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags=tag)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['tags'] = ProductTagModel.objects.all()
        data['categories'] = CategoryModel.objects.all()
        return data


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['products'] = ProductModel.objects.all().exclude(id=self.object.pk)[:4]
        return data
