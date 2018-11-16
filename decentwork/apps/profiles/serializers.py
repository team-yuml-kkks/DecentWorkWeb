from rest_framework import serializers

from decentwork.apps.common.models import User
from decentwork.apps.profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Provides json serializer for `UserProfile` model"""

    def save(self, first_name: str, last_name: str):
        """Saves user profile.

        Adds to common `User` model first_name and last_name
        and creates User Profile for specific user.

        Args:
            first_name: User's first_name
            last_name: User's last_name
        """
        user = self.validated_data['user']
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user_profile = UserProfile.objects.create(
            user=user,
            city=self.validated_data.get('city', None),
            description=self.validated_data.get('description', None),
            phone_numbers=self.validated_data.get('phone_number', None)
        )

        professions = self.validated_data.get('professions', None)

        if professions is not None:
            for profession in professions:
                user_profile.professions.add(profession)

    class Meta:
        model = UserProfile
        fields = '__all__'
