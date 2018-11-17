from rest_framework import serializers

from decentwork.apps.professions.models import Profession


class ProfessionSerializer(serializers.ModelSerializer):
    """Serialize `Profession` to json."""

    class Meta:
        model = Profession
        fields = '__all__'