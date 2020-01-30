from rest_framework import serializers
from authentication.serializers import UserSerializer
from memes.models import Meme


class MemeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Meme
        fields = '__all__'


class MemeSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Meme
        fields = '__all__'

