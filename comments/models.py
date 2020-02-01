from django.db import models

from TremyServer import settings
from core.models import CreatedModified

# Create your models here.
from memes.models import Meme


class Comment(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)

    class Meta:
        abstract = True


class MemeComment(Comment):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'meme_comments'

    def __str__(self):
        return self.body
