from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.

def product_detail_view(request):
    obj = get_object_or_404(Product, id=2)
    context = {
        "object": obj
    }
    return render(request, "product_detail.html", context)