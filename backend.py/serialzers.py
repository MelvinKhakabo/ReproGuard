#from rest_framework import serializers

from .models import User, HealthResource, PeerMessage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_health_professional']

class HealthResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthResource
        fields = ['id', 'title', 'content', 'user']

class PeerMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeerMessage
        fields = ['id', 'sender', 'content', 'created_at']
