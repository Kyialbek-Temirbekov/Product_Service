from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from .forms import ProductForm
from .forms import RawProductForm

# Create your views here.

class RestProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_create_view(request):
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    # if form.is_valid():
    #     form.save()
    #     form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)

# def product_create_view(request):
#     print(request.POST.get('title'))
#     context = {}
#     return render(request, "product_create.html", context)

# def product_create_view(request):
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": RawProductForm()
#     }
#     return render(request, "product_create.html", context)

def product_detail_view(request):
    obj = get_object_or_404(Product, id=2)
    context = {
        "object": obj
    }
    return render(request, "product_detail.html", context)