from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import SmallIntegerField, FloatField, IntegerField, CharField, \
    ImageField

from shared.django import CSPBaseModel, TimeBaseModel, SlugBaseModel, upload_name_cpu, upload_name_video_card


# Processor
class CentralProcessingUnit(SlugBaseModel, TimeBaseModel, CSPBaseModel):
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
    image = ImageField(upload_to=upload_name_cpu)
    views = IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        db_table = 'cpu'


class VideoCard(SlugBaseModel, TimeBaseModel, CSPBaseModel):
    processor_series = CharField(max_length=300)
    graphics_processing_unit = CharField(max_length=300)
    graphics_processing_unit_frequency = CharField(max_length=300)
    video_memory_type = CharField(max_length=300)
    image = ImageField(upload_to=upload_name_video_card)
    views = IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        db_table = 'video_card'
