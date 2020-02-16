from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemeCommentView.as_view(), name='meme_comment_view'),
    path('<int:meme_comment_id>/', views.MemeCommentDetail.as_view(), name="meme_comment_detail")
]