#views for application, health resources, and peer messaging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HealthResource, PeerMessage
from .serializers import HealthResourceSerializer, PeerMessageSerializer

class HealthResourceViewSet(viewsets.ModelViewSet):
    queryset = HealthResource.objects.all()
    serializer_class = HealthResourceSerializer
    permission_classes = [IsAuthenticated]

class PeerMessageViewSet(viewsets.ModelViewSet):
    queryset = PeerMessage.objects.all()
    serializer_class = PeerMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
