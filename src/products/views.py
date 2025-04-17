from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from .forms import RawProductForm

# Create your views here.

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "product_create.html", context)

# def product_create_view(request):
#     print(request.POST.get('title'))
#     context = {}
#     return render(request, "product_create.html", context)

def product_create_view(request):
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": RawProductForm()
    }
    return render(request, "product_create.html", context)

def product_detail_view(request):
    obj = get_object_or_404(Product, id=2)
    context = {
        "object": obj
    }
    return render(request, "product_detail.html", context)