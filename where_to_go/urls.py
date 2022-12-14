"""where_to_go URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from places.views import get_places, get_place_by_id

def index(request):
    context = {}
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_places),
    path('places/<int:place_id>', get_place_by_id, name='place_by_id')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
