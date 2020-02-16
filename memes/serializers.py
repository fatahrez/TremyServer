from rest_framework import serializers
from authentication.serializers import UserSerializer
from comments.models import MemeComment
from comments.serializers import MemeCommentSerializer
from memes.models import Meme


class MemeSerializer(serializers.ModelSerializer):
    meme_comments_count = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Meme
        fields = '__all__'

    @staticmethod
    def get_meme_comments_count(meme):
        return MemeComment.objects.filter(meme=meme).count()


class MemeSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Meme
        fields = '__all__'


class MemeSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Meme
        exclude = ('user',)

    def validate(self, data):

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit posts from other users')
        return data


class MemeSerializerFull(MemeSerializer):
    meme_comments = MemeCommentSerializer(many=True, read_only=True)
