from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from users import views

urlpatterns = [
    path('register/', views.UserRegistraitionView.as_view()),
    path('login/', views.LoginView.as_view()),
]
