from rest_framework import serializers

from decentwork.apps.engagments.models import Engagment


class EngagmentSerializer(serializers.ModelSerializer):
    """Serialize `Engagment` to json."""

    class Meta:
        model = Engagment
        fields = '__all__'
