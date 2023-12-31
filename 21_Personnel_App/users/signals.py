
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import  Token
from .models import Profile

@receiver(post_save, sender=User)
def create_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created=False, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

