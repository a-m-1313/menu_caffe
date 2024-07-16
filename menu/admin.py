
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django import forms
from django.db.models import Count
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from . import models




@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    model = models.Product
    list_display = ['name','price','description','category']
    search_fields = ['name__istartswith']
    list_per_page = 10
    

    list_editable = ['price',]
    

   
    
    
class MyModelForm(forms.ModelForm):
    CAFEE = _('Caffe')
    ICEPACK = _('IcePack')
    DESSERT = _('Dessert')
    SNACK = _('Snack')
    SMOOTHIE =_('Smoothie')
    MOCKTAILE =_('Mocktile')
    LIST_NAME = [
        (CAFEE, _('Caffe')),
        (ICEPACK, _('IcePack')),
        (DESSERT, _('Dessert')),
        (SNACK, _('Snack')),
        (SMOOTHIE, _('Smoothie')),
        (MOCKTAILE, _('Mocktile')),
    ]

    name = forms.ChoiceField(choices=LIST_NAME)




class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('name','description','top_product','num_of_product' )
    form = MyModelForm


    def get_queryset(self, request):
        return super().get_queryset(request) \
            .prefetch_related('product_category') \
            .annotate(product_count=Count('product_category'))

    @admin.display(ordering='product_count', description=_('product count'))
    def num_of_product(self, product: models.Category):
        url = (
            reverse('admin:menu_product_changelist')
            +
            '?'
            +
            urlencode({
                'category__id': product.id
            })
        )
        return format_html('<a href="{}">{}</a>', url, product.product_count)

admin.site.register(models.Category, CategoryAdmin)

        
       
    
        
        
    
    



