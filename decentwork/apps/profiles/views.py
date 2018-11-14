from rest_framework import viewsets

from decentwork.apps.profiles.models import UserProfile
from decentwork.apps.profiles.serializers import UserProfileSerializer


class UserProfileSet(viewsets.ModelViewSet):
    """ViewSet for UserProfile model."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(
            self.request.data['first_name'],
            self.request.data['last_name']
        )
