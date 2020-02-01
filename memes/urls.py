from django.urls import path

from memes import views

urlpatterns = [
    path('', views.MemeView.as_view()),
]
