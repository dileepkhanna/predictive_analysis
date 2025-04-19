from django.urls import path
from . import views

urlpatterns = [
    path('customer_home/', views.customer_home),
    path('customer_register/', views.customer_register),
    path('customer_login/', views.customer_login),
    path('customer_logout/', views.customer_logout),
    path('customer_initiation_form/', views.customer_initiation_form),
    path('customer_updated_table/', views.customer_updated_table),
    path('request_estimation/<int:id>/', views.request_estimation),
    path('receive_estimation/', views.receive_estimation),
    path('accept_work/<int:id>/', views.accept_work),
]
