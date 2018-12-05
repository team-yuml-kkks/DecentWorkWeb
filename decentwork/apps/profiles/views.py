from rest_framework import authentication, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from decentwork.apps.profiles.models import UserProfile
from decentwork.apps.profiles.serializers import (UserNamesSerializer,
                                                  UserProfileSerializer,
                                                  UserProfileList)


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


class Get4UserProfiles(APIView):
    authentication_classes = []

    def get(self, request, format=None):
        """
        Get four random user profiles. Two with professions not equal null
        and two with professions equal null with corresponding to owner of profile
        first_name and last_name.
        """
        profiles = UserProfile.objects.filter(
            professions=None
        ).select_related('user').only(
            'user__first_name', 'user__last_name'
        ).order_by('?')[:2]

        profiles2 = UserProfile.objects.exclude(
            professions=None
        ).select_related('user').only(
            'user__first_name', 'user__last_name'
        ).order_by('?')[:2]

        profiles_all = profiles.union(profiles2)
        profiles_response = []

        for profile in profiles_all:
            profiles_response.append({
                'user': {
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name
                },
                'city': profile.city,
                'professions': list(profile.professions.all())
            })

        serializer = UserProfileList(profiles_response, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
