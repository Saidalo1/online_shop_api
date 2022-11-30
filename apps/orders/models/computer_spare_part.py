from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CASCADE, ForeignKey, SmallIntegerField, FloatField, IntegerField, Model, CharField, \
    ImageField

from orders.models.computer_spare_part_handbook import Type
from shared.django import CSPBaseModel, TimeBaseModel, SlugBaseModel


# Processor
class CentralProcessingUnit(CSPBaseModel, TimeBaseModel, SlugBaseModel):
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
    image = ImageField(upload_to='cpu/image/default-image')
    views = IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)


class VideoCard(CSPBaseModel, TimeBaseModel, SlugBaseModel):
    processor_series = CharField(max_length=300)
    graphics_processing_unit = CharField(max_length=300)
    graphics_processing_unit_frequency = CharField(max_length=300)
    video_memory_type = CharField(max_length=300)
    image = ImageField(upload_to='video-card/image/default-image')
    views = IntegerField(default=0)

    def __str__(self):
        return self.name
