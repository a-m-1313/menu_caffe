from django.urls import path
from . views import ProductList, IcePackList, DessertList, SmoothieList , MocktileList, SnackList, CaffeList

urlpatterns = [
    path('', ProductList.as_view(), name='menu'),
    path('Caffe_menu', CaffeList.as_view(), name='caffe_menu'),
    path('Icepack_menu', IcePackList.as_view(), name='icepack_menu'),
    path('Dessert_menu', DessertList.as_view(), name='dessert_menu'),
    path('Smoothie_menu', SmoothieList.as_view(), name='smoothie_menu'),
    path('Mocktile_menu', MocktileList.as_view(), name='mocktile_menu'),
    path('Snack_menu', SnackList.as_view(), name='snack_menu'),
   
    
    
]
