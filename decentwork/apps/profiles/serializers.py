from rest_framework import serializers

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.professions.models import Profession
from decentwork.apps.profiles.models import UserProfile


class UserNamesSerializer(serializers.ModelSerializer):
    """Provides additional information for UserProfileSerializer."""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    """Provides json serializer for `UserProfile` model."""
    professions = serializers.SlugRelatedField(
        many=True,
        queryset=Profession.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    user = UserNamesSerializer(
        allow_null=True,
        required=False
    )

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        """Creates user profile and updates user object if necessary."""
        professions = None

        if 'professions' in validated_data:
            professions = validated_data.pop('professions')

        auth_user = self.context['request'].user

        if 'user' in validated_data:
            user = validated_data.pop('user')
            User.objects.filter(id=auth_user.id).update(**user)
            user = User.objects.get(id=auth_user.id)
        else:
            user = auth_user

        validated_data['user'] = user
        profile = UserProfile.objects.create(**validated_data)

        if professions is not None:
            profile.professions.add(*professions)

        return profile


class UserProfileList(serializers.ModelSerializer):
    user = UserNamesSerializer(
        allow_null=True,
        required=False
    )

    professions = serializers.SlugRelatedField(
        many=True,
        queryset=Profession.objects.all(),
        allow_null=True,
        required=False,
        slug_field='name'
    )

    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        allow_null=True,
        required=False,
        slug_field='name'
    )

    class Meta:
        model = UserProfile
        fields = ('user', 'professions', 'city')
