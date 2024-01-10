"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from api.views import VehicleViewSet

router = routers.DefaultRouter()
router.register(r"vehicles", VehicleViewSet, basename="vehicle")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # Router will generate all the routes for us
    path("api-auth/", include("rest_framework.urls")),  # This is for the browsable API
]
