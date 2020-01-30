from django.urls import path

from appprofile import views

urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('<int:profile_id>', views.ProfileDetail.as_view()),
]