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

    def update(self, instance, validated_data):
        user = validated_data.get('user', None)

        if user:
            instance.user.first_name = user.get('first_name', '')
            instance.user.last_name = user.get('last_name', '')

        instance.city = validated_data.get('city', None)
        instance.phone_numbers = validated_data.get('phone_numbers', None)
        instance.professions.set(validated_data.get('professions', []))
        instance.description = validated_data.get('description', None)
        instance.user.save()
        instance.save()
        return instance


class UserProfileList(serializers.ModelSerializer):
    user = UserNamesSerializer()

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
