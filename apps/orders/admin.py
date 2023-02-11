from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm
from django_admin_hstore_widget.forms import HStoreFormField
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter

from orders.models import Product, ProductImages, Category, SubCategory, Company, ProductRating, ProductComments, Basket, \
    Order, Payment
from shared.django import delete_all_photos, delete_main_photo


class ProductAdminForm(ModelForm):
    details = HStoreFormField()

    class Meta:
        model = Product
        exclude = ()


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    search_fields = ('__all__',)
    readonly_fields = ('views',)
    list_display = ('name', 'price', 'category')
    list_filter = (
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter), ('price', NumericRangeFilter),
        ('count', NumericRangeFilter),
        ('views', NumericRangeFilter),
        'category',
    )
    form = ProductAdminForm
    exclude = ()

    def delete_model(self, request, obj):
        delete_main_photo(Product, obj.pk)
        delete_all_photos(ProductImages, obj.pk)
        super().delete_model(request, obj)

    def render_change_form(self, request, context, add=False, change=False, form_url="", obj=None):
        # product delete main image
        # def update(self, instance, validated_data):
        #     old_image = instance.image.file.name
        #     new_image = validated_data['image']
        #     if has_difference_images(old_image, new_image):
        #         # Delete old photo
        #         delete_main_photo(Images, instance.id)
        #         return super().update(instance, validated_data)
        #     # if hasn't differences between images
        #     return Images.objects.get(id=instance.id)
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ()


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    exclude = ()


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    exclude = ()


@admin.register(ProductImages)
class ImagesAdmin(ModelAdmin):
    exclude = ()


@admin.register(ProductRating)
class RatingAdmin(ModelAdmin):
    exclude = ()


@admin.register(ProductComments)
class CommentsAdmin(ModelAdmin):
    exclude = ()


@admin.register(Basket)
class BasketAdmin(ModelAdmin):
    exclude = ()


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    exclude = ()


@admin.register(Payment)
class PaymentsAdmin(ModelAdmin):
    exclude = ()
