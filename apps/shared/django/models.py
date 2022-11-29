from django.db.models import CharField, SlugField, Model, DateTimeField


class SlugBaseModel(Model):
    slug = SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True


class CSPBaseModel(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=1000)

    class Meta:
        abstract = True


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
