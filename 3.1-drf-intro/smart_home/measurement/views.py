# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import (
    SensorDetailSerializer,
    SensorsSerializer,
    MeasurementSerializer,
    MeasurementDetailSerializer,
)


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        Sensor.objects.create(
            name=request.POST.get("name"), description=request.POST.get("description")
        )
        return Response({"status": "OK"})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        sensor.description = request.data["description"]
        sensor.save()
        return Response({"status": "OK"})


class MeasurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

    def post(self, request):
        Measurement.objects.create(
            sensor_id=request.POST.get("sensor"),
            temperature=request.POST.get("temperature"),
        )
        return Response({"status": "OK"})
