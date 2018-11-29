from typing import Dict, Optional

from allauth.account.adapter import get_adapter
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.contrib.auth import authenticate
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework import authentication, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from decentwork.apps.common.models import User
from decentwork.apps.common.serializers import (UserLoginSerializer,
                                                UserRegisterSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User common model."""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'retrieve':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class UserApiLogin(APIView):
    authentication_classes = ()

    def post(self, request, format=None) -> Response:
        """Tries to authenticate user."""
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.filter(
                email=request.data['email']).first()

            if user is not None:
                user = authenticate(
                    username=user.username,
                    password=request.data['password']
                )

                if user is not None:
                    return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenSignIn(APIView):
    """Handle user sign in from mobile device."""
    authentication_classes = ()

    def post(self, request, format=None) -> Response:
        """Creates user with data from Google oauth2 token when email doesn't exist in database.
        
        Returns:
            Response with UserLoginSerializer data and status code equal 200 if everything went okay.
            Response with status code equal 400 when user didn't send idToken with request.
            Response with status code equal 401 when token is invalid.
        """
        token = request.data.get('idToken', None)
        
        if token:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                return Response("Token jest zły", status=status.HTTP_401_UNAUTHORIZED)

            email = idinfo['email']
            user =  User.objects.filter(email=email).first()

            if user is None:
                new_user = self._create_user(idinfo)

                social_user = SocialAccount.create(
                    user=user,
                    provider='google',
                    uid=idinfo['sub'],
                    extra_data=idinfo
                )

                serializer = self._serialize_user_data(new_user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = self._serialize_user_data(user)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("Brak tokenu", status=status.HTTP_400_BAD_REQUEST)

    def _serialize_user_data(self, user: User) -> UserLoginSerializer:
        """Serialize user data.
        
        Args:
            user: User object to serialize.
        """
        return UserLoginSerializer(
            id=user.id,
            email=user.email,
        )

    def _create_user(self, idinfo: Dict[str, str]) -> User:
        """Creates new User.
        
        Args:
            ididnfo: Information from Google about user.
        
        Returns:
            Saved new user.
        """
        user = User()
        user.set_unusable_password(True)
        user.email = idinfo['email']
        user.username = idinfo['email']
        user.first_name = idinfo['given_name']
        user.last_name = idinfo['family_name']
        user.save()

        return user
