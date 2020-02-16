from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.models import MemeComment
from comments.serializers import MemeCommentSerializerCreate, MemeCommentSerializer, MemeCommentSerializerUpdate


# Create your views here.
class MemeCommentView(APIView):

    @staticmethod
    def post(request):
        serializer = MemeCommentSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(MemeCommentSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemeCommentDetail(APIView):

    @staticmethod
    def patch(request, meme_comment_id):
        meme_comment = get_object_or_404(MemeComment, pk=meme_comment_id)
        serializer = MemeCommentSerializerUpdate(meme_comment, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(MemeCommentSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, meme_comment_id):
        meme_comment = get_object_or_404(MemeComment, pk=meme_comment_id)
        if meme_comment.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        meme_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)