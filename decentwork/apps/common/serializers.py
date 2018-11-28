from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from decentwork.apps.common.models import User


user_fields = {
    'id': {'read_only': True},
    'email': {'allow_null': False, 'required': True},
    'password': {'write_only': True},
    'token': {'read_only': True}
}


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

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

    def get_token(self, obj):
        return Token.objects.filter(user__id=obj.id).values('key').first()

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'token')
        extra_kwargs = user_fields


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return Token.objects.filter(user__email=obj['email']).values('key').first()

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'token')
        extra_kwargs = user_fields
