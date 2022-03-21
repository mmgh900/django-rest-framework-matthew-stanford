from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.UserRegistraitionView.as_view()),
]
