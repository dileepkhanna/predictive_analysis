from django.urls import path
from . import views

urlpatterns = [
    path('manager_home/', views.manager_home),
    path('manager_register/', views.manager_register),
    path('manager_login/', views.manager_login),
    path('manager_logout/', views.manager_logout),
    path('customer_initiation_table/', views.customer_initiation_table),
    # path('update/<int:id>/', views.update),
    path('update1/<int:id>/', views.update1),
    path('content_update/<str:customer_email>/', views.content_update),
    path('show_customer/', views.show_customer),
    path('send_customer/<int:id>/', views.send_customer),
    path('material_details/', views.material_details),
    path('material_details_form/', views.material_details_form),
    path('price_analyse/', views.price_analyse),
    path('algorithm/', views.algorithm),
    path('apply_algorithm/<int:id>/', views.apply_algorithm),
    path('price_prediction/', views.price_prediction),
    path('send_cost/<int:id>/', views.send_cost),
]
