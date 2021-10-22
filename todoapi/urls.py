"""todoapi URL Configuration"""

from django.urls import path, include
from rest_framework import routers
from todoapi.api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'ping', views.PingViewSet, basename='ping')

urlpatterns = [
    path('', include(router.urls)),
]
