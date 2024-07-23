from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "description"]


class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["sensor", "temperature", "created_at"]


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["temperature", "created_at"]


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "measurements"]
