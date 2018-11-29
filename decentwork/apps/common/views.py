from django.conf import settings
from django.contrib.auth import authenticate
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework import authentication, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = ()

    def post(self, request, format=None) -> Response:
        token = request.data.get('idToken', None)
        
        if token:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                return Response("Token jest zły", status=status.HTTP_401_UNAUTHORIZED)

            userid = idinfo['sub']
            print(userid)

        return Response("Brak tokenu", status=status.HTTP_400_BAD_REQUEST)
