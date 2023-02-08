from django.core.validators import MinValueValidator
from django.db.models import CASCADE, ForeignKey, Model, CharField, ImageField, \
    FloatField, IntegerField, TextField, TextChoices, BooleanField, SET_NULL
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django import TimeBaseModel, upload_other_images_product_url


class Category(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Categories"


class SubCategory(Model):
    name = CharField(max_length=50)
    category = ForeignKey('orders.Category', CASCADE)

    def __str__(self):
        return f'{self.category.name} --> {self.name}'

    class Meta:
        db_table = 'sub_category'
        verbose_name_plural = "Sub Categories"


class Company(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'
        verbose_name_plural = "Companies"


class ProductImages(Model):
    product = ForeignKey('orders.Product', CASCADE)
    image = ImageField(upload_to=upload_other_images_product_url)

    class Meta:
        db_table = 'images'
        verbose_name_plural = "Images"


class Rating(Model):
    product = ForeignKey('orders.Product', CASCADE)
    rating = IntegerField(default=0)
    user = ForeignKey('users.User', CASCADE)

    def __str__(self):
        return f"{self.product} {self.rating} {self.user}"

    class Meta:
        db_table = 'rating'


class ProductComments(TimeBaseModel, MPTTModel):
    product = ForeignKey('orders.Product', CASCADE)
    text = TextField(max_length=500)
    user = ForeignKey('users.User', CASCADE)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return f"{self.user} {self.product}"

    class MPTTMeta:
        order_insertion_by = ['name']

    def children(self):
        return ProductComments.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    class Meta:
        db_table = 'comments'
        verbose_name_plural = "Comments"


class Basket(Model):
    user = ForeignKey('users.User', CASCADE)
    count = IntegerField(default=0, validators=(MinValueValidator(0),))
    product = ForeignKey('orders.Product', CASCADE)

    @property
    def total_price_of_products(self):
        return self.product.total_price * self.count

    def __str__(self):
        return f"{self.user} {self.product} {self.count}"

    class Meta:
        db_table = 'basket'


class Order(TimeBaseModel):
    class StatusChoices(TextChoices):
        ordered = 'ordered', 'Ordered'
        paid = 'paid', 'Paid'
        delivered = 'delivered', 'Delivered'
        received = 'received', 'Received'

    user = ForeignKey('users.User', CASCADE)
    count = IntegerField(default=0)
    product = ForeignKey('orders.Product', SET_NULL, null=True)
    status = CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.ordered)

    def __str__(self):
        return f"{self.user} {self.product} {self.status}"

    class Meta:
        db_table = 'order'


class Payment(TimeBaseModel):
    class PaymentType(TextChoices):
        click = 'click'

    user = ForeignKey('users.User', CASCADE)
    amount = FloatField(default=0)
    type = CharField(max_length=85, choices=PaymentType.choices)

    def __str__(self):
        return f"{self.user} {self.amount}"

    class Meta:
        db_table = 'payments'
