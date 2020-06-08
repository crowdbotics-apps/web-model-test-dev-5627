from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HJGhjkhViewSet

router = DefaultRouter()
router.register("hjghjkh", HJGhjkhViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
