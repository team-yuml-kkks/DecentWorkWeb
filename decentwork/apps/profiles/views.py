from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated

from decentwork.apps.profiles.models import UserProfile
from decentwork.apps.profiles.serializers import UserProfileSerializer


class UserProfileSet(viewsets.ModelViewSet):
    """ViewSet for UserProfile model."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer: UserProfileSerializer):
        is_mobile = self.request.data.get('is_mobile', False)

        if is_mobile:
            serializer.save(
                self.request.data['first_name'],
                self.request.data['last_name']
            )
        else:
            if self.request.user:
                serializer.save(
                    self.request.data['first_name'],
                    self.request.data['last_name'],
                    web_user=self.request.user
                )
            else:
                raise NotAuthenticated("User is not logged in.", 401)
