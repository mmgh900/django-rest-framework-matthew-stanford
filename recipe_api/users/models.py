from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # To do something after user save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
