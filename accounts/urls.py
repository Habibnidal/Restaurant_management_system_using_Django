from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registration, name='register'),
    path('login/', views.user_login, name='login'),

    # NEW DASHBOARD ROUTES
    path('dashboard/vendor/', views.vendor_dashboard, name='vendor_dashboard'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),

    # Old dashboard — optional
    path('logout/', views.user_logout, name='logout'),
    path('update/',views.update, name='update'),
    path('forgot_password/', views.forgot_password, name='forgot_password')
]
