from django.urls import path

from authentication import views

urlpatterns = [
    path('register', views.RegistrationAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('user', views.UserRetrieveUpdateAPIView.as_view(), name="user")
]
