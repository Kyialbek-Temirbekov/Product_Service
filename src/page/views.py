from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs ):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs ):
    my_context = {
        "address": "Budapesht 122",
        "phone": 1222,
        "list": [123,4242,312,"Abc"]
    }
    return render(request, "contact.html", my_context)

def view(request, *args, **kwargs ):
    return HttpResponse(f"<h1>Hello {request.user}</h1>")