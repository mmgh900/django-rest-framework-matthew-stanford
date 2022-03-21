from urllib.request import Request
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.views import APIView

class UserRegistraitionView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, serializer, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=self.request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            data = {'token': token}
        else:
            data = serializer.errors
        return Response(data=data, status=201)


class LoginView(APIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        return obtain_auth_token(request= request._request)
