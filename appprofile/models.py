from django.db import models


# Create your models here.
from TremyServer import settings


class Profile(models.Model):
    bio = models.CharField(blank=True, max_length=500)
    image = models.ImageField(blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.email
