from rest_framework import serializers

from decentwork.apps.engagments.models import Engagment


class EngagmentSerializer(serializers.ModelSerializer):
    """Serialize `Engagment` to json."""
    profession = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Engagment
        fields = ('id', 'title', 'profession')
