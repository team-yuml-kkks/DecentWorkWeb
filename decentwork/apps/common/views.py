from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from decentwork.apps.common.models import User
from decentwork.apps.common.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User common model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Create user."""
        password = self.request.data['password']

        serializer.save(password=password)
