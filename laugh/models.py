from django.db import models

from authentication.models import User
from core.models import CreatedModified


# Create your models here.
class Laugh(CreatedModified):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey('memes.Meme', on_delete=models.CASCADE)
