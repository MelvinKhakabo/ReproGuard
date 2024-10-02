#set up routing for api

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthResourceViewSet, PeerMessageViewSet

router = DefaultRouter()
router.register(r'health-resources', HealthResourceViewSet)
router.register(r'peer-messages', PeerMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
