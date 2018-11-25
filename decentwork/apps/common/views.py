from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from decentwork.apps.common.models import User
from decentwork.apps.common.serializers import (UserLoginSerializer,
                                                UserRegisterSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User common model."""

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer: UserRegisterSerializer):
        """Creates user.
        
        Raises:
            ParseError: When no email or password in post parameters.
        """
        password = self.request.data.get('password', None)
        email = self.request.data.get('email', None)

        if password is None or email is None:
            raise ParseError()
        
        User.objects.create_user(username=email, email=email, password=password)


class UserApiLogin(APIView):

    def post(self, request, format=None) -> Response:
        """Tries to authenticate user."""
        password = request.data.get('password', None)
        email = request.data.get('email', None)

        if not email or not password:
            return Response("Brak hasła lub adresu e-mail.", status=status.HTTP_400_BAD_REQUEST)

        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.filter(email=email).first()

            if user is not None:
                user = authenticate(
                    username=user.username,
                    password=password
                )

                if user is not None:
                    return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
