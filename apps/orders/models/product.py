from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import HStoreField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import FloatField, IntegerField, CharField, \
    ImageField, Manager, ForeignKey, CASCADE

from shared.django import TimeBaseModel, upload_image_product_url


class ProductManager(Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(count__gt=0)


class Product(TimeBaseModel):
    name = CharField(max_length=255)
    description = RichTextField(max_length=7500)
    count = IntegerField(default=0)
    price = FloatField(default=0,
                       validators=[
                           MaxValueValidator(1000000000.00),
                           MinValueValidator(0)
                       ])
    image = ImageField(upload_to=upload_image_product_url)
    views = IntegerField(default=0)
    category = ForeignKey('orders.SubCategory', CASCADE)
    details = HStoreField('details of product', default=dict)
    sale_percent = IntegerField(default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
    objects = ProductManager()

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if self.sale_percent > 0:
            return self.price - self.price * self.sale_percent / 100
        return self.price

    class Meta:
        ordering = ('-created_at',)
        db_table = 'product'

