from django.urls import path
from . import views

urlpatterns = [
    path('qmt_home/', views.qmt_home),
    path('qmt_register/', views.qmt_register),
    path('qmt_login/', views.qmt_login),
    path('qmt_logout/', views.qmt_logout),
    path('send_to_analyse/', views.send_to_analyse),
    path('click_to_send/<int:id>/', views.click_to_send),
    path('qmt_material_details/', views.qmt_material_details),
    path('algo/', views.algo),
    path('apply_algo/<int:id>/', views.apply_algo),
    path('desired_land/', views.desired_land),
]
