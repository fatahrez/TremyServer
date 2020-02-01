from rest_framework import serializers

from authentication.serializers import UserSerializer
from comments.models import MemeComment


class MemeCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MemeComment
        fields = '__all__'

