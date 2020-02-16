from django.db import models

from TremyServer import settings
from core.models import CreatedModified

from laugh.models import Laugh


# Create your models here.
class Meme(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    image = models.ImageField(blank=True)

    class Meta:
        default_related_name = 'memes'

    def __str__(self):
        return self.body

    @property
    def get_laughs_count(self):
        return Laugh.objects.filter(meme=self).count()
