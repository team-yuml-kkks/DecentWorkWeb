from django.core.exceptions import ValidationError
from rest_framework import serializers

from decentwork.apps.common.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    def validate_email(self, value):
        """Validate is unique."""
        user = User.objects.filter(email=value)

        if user:
            raise ValidationError('Taki email już istnieje.')

        return value

    def save(self, password):
        email = self.validated_data['email']

        User.objects.create_user(username=email, email=email, password=password)

    class Meta:
        model = User
        fields = ('email',)


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)
