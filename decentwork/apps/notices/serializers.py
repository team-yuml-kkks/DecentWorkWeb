from rest_framework import serializers

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.notices.models import Notice, UserAssigned
from decentwork.apps.professions.models import Profession


class NoticeSerializer(serializers.ModelSerializer):
    """Serialize `Notice` to json."""
    profession = serializers.SlugRelatedField(
        queryset=Profession.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        slug_field='name'
    )

    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='email',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Notice
        fields = ('id', 'profession', 'owner', 'city', 'title', 'description', 'created')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class AssignNoticeSerializer(serializers.ModelSerializer):
    """Assign notice to user which wants to do this notice."""
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='id',
        allow_null=True,
        required=False
    )

    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserAssigned
        fields = ('notice', 'user', 'email')


class CheckAssignSerializer(serializers.Serializer):
    is_assigned = serializers.BooleanField(default=False)
