from rest_framework import serializers

from appprofile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'image',)
