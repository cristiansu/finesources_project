from django.urls import path
from .views import *


app_name='listings'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>', product_list, name='product_list_by_category')
]