from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from memes.models import Meme
from memes.serializers import MemeSerializer, MemeSerializerCreate


# Create your views here.
class MemeView(APIView):

    @staticmethod
    def get(request):
        memes = Meme.objects.all()
        # memes = meme_filter(request, posts)
        if type(memes) == Response:
            return memes
        return Response(MemeSerializer(memes, many=True).data)

    @staticmethod
    def post(request):
        serializer = MemeSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(MemeSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


