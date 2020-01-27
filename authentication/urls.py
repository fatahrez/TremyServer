from django.urls import path

from authentication import views

urlpatterns = [
    path('register', views.RegistrationAPIView.as_view(), name="register"),
]