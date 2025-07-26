from django.urls import path
from . import views

urlpatterns = [
    path('vendor_home/', views.vendor_home),
    path('vendor_register/', views.vendor_register),
    path('vendor_login/', views.vendor_login),
    path('vendor_logout/', views.vendor_logout),
    path('received_material_details/', views.received_material_details),
    path('send_to_supply/<int:id>/', views.send_to_supply),
    path('supply_materials/', views.supply_materials),
    path('send_to_customer/<int:id>/', views.send_to_customer),
    path('view_details/', views.view_details),
]
