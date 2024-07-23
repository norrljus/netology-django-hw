from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "сенсор"
        verbose_name_plural = "Сенсоры"

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="measurement",
        verbose_name="Измерение",
    )
    temperature = models.FloatField(verbose_name="Температура")
    created_tm = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время")

    class Meta:
        verbose_name = "показание"
        verbose_name_plural = "Показания"
