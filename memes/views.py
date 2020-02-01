from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from memes.models import Meme
from memes.serializers import MemeSerializer, MemeSerializerCreate, MemeSerializerFull, MemeSerializerUpdate


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


class MemeDetail(APIView):

    @staticmethod
    def get(request, meme_id):
        meme = get_object_or_404(Meme, pk=meme_id)

        return Response(MemeSerializerFull(meme).data)

    @staticmethod
    def patch(request, meme_id):
        meme = get_object_or_404(Meme, pk=meme_id)

        serializer = MemeSerializerUpdate(meme, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(MemeSerializerFull(meme.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, meme_id):
        meme = get_object_or_404(Meme, pk=meme_id)

        if meme.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
