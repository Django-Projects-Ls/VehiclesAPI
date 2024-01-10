from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format and vice versa."""

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "name",
            "model",
            "price",
            "speed",
            "passengers",
            "year",
        ]
