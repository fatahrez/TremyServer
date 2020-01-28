from django.db import models


# Create your models here.
class Profile(models.Model):
    bio = models.CharField(blank=True, max_length=500)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.email
