from django.shortcuts import render, get_object_or_404
from . import models




def product_all(request):
    products = models.Product.products.all()
    return render(request, 'store/home.html', {'products' : products})


def category_list(request, category_slug):
    category = get_object_or_404(models.Category, slug = category_slug)
    products = models.Product.objects.filter(category = category)
    return render(request, 'store/products/category.html', {'category' : category, 'products' : products})



def product_detail(request, slug):
    product = get_object_or_404(models.Product, slug = slug, in_stock = True)
    return render(request, 'store/products/product.html', {'product':product})

