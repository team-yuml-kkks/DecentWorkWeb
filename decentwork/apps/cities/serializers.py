from rest_framework import serializers

from decentwork.apps.cities.models import City


class CitySerializer(serializers.ModelSerializer):
    """Serialize `City` to json."""

    class Meta:
        model = City
        fields = '__all__'
