from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from appprofile.models import Profile

# Create your views here.
from appprofile.serializers import ProfileSerializer, ProfileSerializerUpdate
from authentication.serializers import LoginSerializer


class ProfileView(APIView):

    @staticmethod
    def get(self):
        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)


class ProfileDetail(APIView):

    @staticmethod
    def patch(request, profile_id):
        profile = get_object_or_404(Profile, pk=profile_id)

        if profile.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProfileSerializerUpdate(profile, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            profile = serializer.save()
            return Response(LoginSerializer(profile.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
