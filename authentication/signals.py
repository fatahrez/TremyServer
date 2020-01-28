from django.db.models.signals import post_save
from django.dispatch import receiver

from appprofile.models import Profile
from authentication.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
