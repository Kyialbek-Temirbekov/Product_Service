"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from page.views import home_view, contact_view
from products.views import product_detail_view, product_create_view, RestProductList
from django.urls import path

urlpatterns = [
    path('rest/', RestProductList.as_view(), name='rest'),
    path('product/', product_detail_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('contact/', contact_view, name='contact'),
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]
