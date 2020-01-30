from authentication import serializers
from authentication.serializers import UserSerializer
from memes.models import Meme


class MemesSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Meme
        fields = '__all__'
