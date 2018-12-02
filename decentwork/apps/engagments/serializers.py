from rest_framework import serializers

from decentwork.apps.cities.models import City
from decentwork.apps.common.models import User
from decentwork.apps.engagments.models import Engagment
from decentwork.apps.professions.models import Profession


class EngagmentSerializer(serializers.ModelSerializer):
    """Serialize `Engagment` to json."""
    profession = serializers.SlugRelatedField(
        queryset=Profession.objects.all(),
        slug_field='name'
    )

    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        slug_field='name'
    )

    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='email'
    )

    class Meta:
        model = Engagment
        fields = ('id', 'title', 'profession', 'owner', 'city', 'title', 'description', 'created')
        extra_kwargs = {
            'id': {'read_only': True},
            'city': {'required': False}
        }
