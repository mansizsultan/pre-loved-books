from django.urls import path
from main.views import (show_main, create_product, clear_table, 
    show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('clear_table', clear_table, name='clear_table'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]