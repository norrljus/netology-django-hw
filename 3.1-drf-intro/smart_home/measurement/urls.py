from django.urls import path

from measurement.views import SensorView, MeasurementsView, SensorsView

urlpatterns = [
    path("sensors/", SensorsView.as_view()),
    path("sensors/<pk>/", SensorView.as_view()),
    path("measurements/", MeasurementsView.as_view()),
]
