from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, SlugField, Model, DateTimeField, IntegerField, FloatField
from django.forms import DecimalField
from django.utils.text import slugify


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
