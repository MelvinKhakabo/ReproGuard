#models for users

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_health_professional = models.BooleanField(default=False)

class HealthResource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')

class PeerMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
