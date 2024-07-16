
from django.utils.translation import gettext as _

from django.views.generic import ListView 
from .models import  Product

class ProductList(ListView):
    model = Product
    template_name = 'home.html'

class CaffeList(ListView):
    model = Product
    template_name = 'caffe.html'
    queryset = Product.objects.filter(category__name=_('Caffe'))
    context_object_name = 'items'

    

class IcePackList(ListView):
    model = Product
    template_name = 'icepack.html'
    queryset = Product.objects.filter(category__name=_('IcePack'))
    context_object_name = 'items'
    

class DessertList(ListView):
    model = Product
    template_name = 'dessert.html'
    queryset = Product.objects.filter(category__name=_('Dessert'))
    context_object_name = 'items'


class SnackList(ListView):
    model = Product
    template_name = 'Snack.html'
    queryset = Product.objects.filter(category__name=_('Snack'))
    context_object_name = 'items'


class SmoothieList(ListView):
    model = Product
    template_name = 'Smoothie.html'
    queryset = Product.objects.filter(category__name=_('Smoothie'))
    context_object_name = 'items'


class MocktileList(ListView):
    model = Product
    template_name = 'Mocktile.html'
    queryset = Product.objects.filter(category__name=_('Mocktile'))
    context_object_name = 'items'

