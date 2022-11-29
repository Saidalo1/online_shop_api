from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, ForeignKey, SmallIntegerField, FloatField, IntegerField, Model, CharField

from orders.models.computer_spare_part_handbook import Type
from shared.django import CSPBaseModel, TimeBaseModel


# Processor
class CentralProcessingUnit(CSPBaseModel, TimeBaseModel):
    type = ForeignKey(Type, on_delete=CASCADE)
    cores = SmallIntegerField(default=0,
                              validators=[
                                  MaxValueValidator(255),
                                  MinValueValidator(1)
                              ])
    flow = SmallIntegerField(default=0,
                             validators=[
                                 MaxValueValidator(256),
                                 MinValueValidator(0)
                             ])
    ghz = FloatField(default=0,
                     validators=[
                         MaxValueValidator(8.429),
                         MinValueValidator(0)
                     ])
    count = IntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class VideoCard(Model):
    name = CharField(max_length=300)
    processor_series = CharField(max_length=300)
    graphics_processing_unit = CharField(max_length=300)
    graphics_processing_unit_frequency = CharField(max_length=300)
    video_memory_type = CharField(max_length=300)

    def __str__(self):
        return self.name
