from django.urls import path

from memes import views

urlpatterns = [
    path('', views.MemeView.as_view()),
    path('<int:meme_id>/', views.MemeDetail.as_view()),
]
