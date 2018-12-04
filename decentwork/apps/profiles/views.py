from rest_framework import authentication, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from decentwork.apps.profiles.models import UserProfile
from decentwork.apps.profiles.serializers import (UserNamesSerializer, 
                                                  UserProfileSerializer)


class UserProfileSet(viewsets.ModelViewSet):
    """ViewSet for UserProfile model."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer: UserProfileSerializer):
        serializer.save()
