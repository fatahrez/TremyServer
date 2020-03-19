from django.db import models

from TremyServer import settings
from authentication.models import User
from core.models import CreatedModified


# Create your models here.
class Laugh(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meme = models.ForeignKey('memes.Meme', on_delete=models.CASCADE)

    def __str__(self):
        return f'meme: {self.meme_id}- value: {self.user_id}'