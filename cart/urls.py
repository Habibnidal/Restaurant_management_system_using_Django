from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:food_item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('increment/<int:item_id>/', views.increment_cart_item, name='increment_cart_item'),
    path('decrement/<int:item_id>/', views.decrement_cart_item, name='decrement_cart_item'),
    path('checkout/', views.checkout, name='checkout')
]
