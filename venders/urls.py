from django.contrib import admin
from django.urls import path
from . import views

app_name = 'venders'

urlpatterns = [
    path('venderregister/', views.venderRegister, name='venderregister'),
    path('<int:id>/', views.vender_details, name='venderdetails'),
    path('addfood/', views.addFood, name='addfood'),
    path('foodedit/<int:id>/', views.food_edit, name='foodedit'),
    path('food/delete/<int:id>/', views.food_delete, name='food_delete'),
    path('franchise/request/<int:vendor_id>/', views.request_franchise, name='request_franchise'),
    path('edit/<int:id>/', views.edit_vendor, name='edit_vendor'),
    path('franchise/<int:vendor_id>/details/', views.franchise_details, name='franchise_details'),
    path('franchise/accepted/',views.accepted_franchises,name='accepted_franchises')
    
]