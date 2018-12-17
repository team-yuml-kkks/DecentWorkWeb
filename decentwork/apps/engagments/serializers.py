from rest_framework import serializers

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.engagments.models import Engagment, UserAssigned
from decentwork.apps.professions.models import Profession


class EngagmentSerializer(serializers.ModelSerializer):
    """Serialize `Engagment` to json."""
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
        model = Engagment
        fields = ('id', 'profession', 'owner', 'city', 'title', 'description', 'created')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class AssignEngagmentSerializer(serializers.ModelSerializer):
    """Assign engagment to user which wants to do this engagment."""
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='id',
        allow_null=True,
        required=False
    )

    class Meta:
        model = UserAssigned
        fields = ('engagment', 'user')
