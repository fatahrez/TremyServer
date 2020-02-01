from rest_framework import serializers

from authentication.serializers import UserSerializer
from comments.models import MemeComment


class MemeCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MemeComment
        fields = '__all__'


class MemeCommentSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = MemeComment
        fields = '__all__'

    def validate(self, user):
        if user != self.context['request'].user:
            raise serializers.ValidationError("you cannot create comments for other users")
        return user
