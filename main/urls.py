from django.urls import path
from main.views import show_main, create_product, clear_table

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('clear_table/', clear_table, name='clear_table'),
]