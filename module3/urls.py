"""
URL configuration for module3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('accounts.urls')),
    path('vender/', include('venders.urls', namespace='venders')),  # Add namespace here
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
]

# Only serve media files in development (not needed with Cloudinary in production)
if settings.DEBUG and hasattr(settings, 'MEDIA_ROOT') and settings.MEDIA_ROOT:
    try:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    except Exception:
        pass  # Skip static media serving if there's an error

