from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import CASCADE, ForeignKey, PositiveIntegerField, Model, CharField, ImageField, \
    FloatField, IntegerField, Index, TextField, DateField, TextChoices
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django import SlugBaseModel, TimeBaseModel
from users.models import User


class Type(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'


class Company(Model):
    name = CharField(max_length=200)
    type = ForeignKey(Type, CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'


class Images(Model):
    image = ImageField(upload_to='csp/images/%y/%m/%d/')
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'images'


class Rating(Model):
    rating = IntegerField(default=0)
    user = ForeignKey(User, on_delete=CASCADE)
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.object_id} {self.rating}"

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'rating'


class Comments(TimeBaseModel, SlugBaseModel, MPTTModel):
    text = TextField(max_length=500)
    user = ForeignKey(User, CASCADE)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.object_id} {self.user} {self.text} {self.created_at}"

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'comments'


class Sales(Model):
    percent = FloatField(default=0)
    title = CharField(max_length=200)
    description = TextField(max_length=1000)
    from_date = DateField(auto_now=True)
    to_date = DateField(auto_now=True)
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.title} {self.percent} {self.description} {self.from_date} {self.to_date}"

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'sales'


class Basket(Model):
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = ForeignKey(User, on_delete=CASCADE)
    count = IntegerField(default=0)

    def __str__(self):
        return f"{self.object_id} {self.user} {self.count}"

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'basket'


class Order(Model):
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = ForeignKey(User, on_delete=CASCADE)
    count = IntegerField(default=0)
    # status
    # 1-ordered
    # 2-paid
    # 3-delevired
    # 4-received
    status = IntegerField(default=0)

    def __str__(self):
        return f"{self.object_id} {self.user} {self.count} {self.status}"

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'order'


class Payments(Model):
    class PaymentType(TextChoices):
        click = 'click'

    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = ForeignKey(User, on_delete=CASCADE)
    amount = FloatField(default=0)
    type = CharField(PaymentType, max_length=85, choices=PaymentType.choices)

    def __str__(self):
        return f"{self.object_id} {self.user} {self.amount}"

    class Meta:
        indexes = [
            Index(fields=["content_type", "object_id"]),
        ]
        db_table = 'payments'
