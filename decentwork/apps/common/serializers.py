from django.core.exceptions import ValidationError
from rest_framework import serializers

from decentwork.apps.common.models import User
from decentwork.apps.common.selectors import (get_token_by_email,
                                              get_token_by_id,
                                              get_id_by_email)


user_fields = {
    'id': {'read_only': True},
    'email': {'allow_null': False, 'required': True},
    'password': {'write_only': True},
    'token': {'read_only': True}
}


class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return get_token_by_email(obj['email'])

    def get_id(self, obj):
        return get_id_by_email(obj['email'])

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'token')
        extra_kwargs = user_fields


class GoogleTokenSerializer(serializers.ModelSerializer):
    """Handle response for Google oauth2 token sign in from mobile."""
    id = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return get_token_by_email(obj['email'])

    def get_id(self, obj):
        return get_id_by_email(obj['email'])

    class Meta:
        model = User
        fields = ('id', 'email', 'token')
