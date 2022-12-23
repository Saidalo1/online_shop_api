from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, SlugField, Model, DateTimeField, IntegerField, FloatField
from django.forms import DecimalField
from django.utils.text import slugify


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += f'{self.__class__.objects.filter(slug=self.slug).count()}'
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class CSPBaseModel(Model):
    description = CharField(max_length=1000)
    count = IntegerField(default=0)
    price = FloatField(default=0,
                       validators=[
                           MaxValueValidator(100000000.00),
                           MinValueValidator(0)
                       ])

    class Meta:
        abstract = True


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
