from django.core.exceptions import ValidationError
from rest_framework import serializers

from decentwork.apps.common.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    def validate_email(self, value: str) -> str:
        """Validate if email is unique.

        Returns:
            If email is unique returns it.

        Raises:
            ValidationError: When email is not unique.
        """
        user = User.objects.filter(email=value)

        if user:
            raise ValidationError('Taki email już istnieje.')

        return value


    class Meta:
        model = User
        fields = ('email',)


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)
