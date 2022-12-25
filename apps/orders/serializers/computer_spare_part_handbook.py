from django.contrib.contenttypes.models import ContentType
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer, ValidationError

from orders.models import Type, Company, Images, Rating, Comments, Sales, Basket, Order, Payments
from shared.django import GetUserNameSerializer, has_difference_images, delete_main_photo


class TypeModelSerializer(ModelSerializer):
    class Meta:
        model = Type
        exclude = ()


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()


class ImagesCreateModelSerializer(ModelSerializer):

    def get_validators(self):
        data = self.context['request'].data
        model_id = data['content_type']
        if model_name := ContentType.objects.filter(pk=model_id).first():
            if model_name.model_class().objects.filter(id=data['object_id']).exists():
                return super().get_validators()
            raise ValidationError("Object not found", 404)
        raise ValidationError("Page not found", 404)

    class Meta:
        model = Images
        exclude = ()


class ImagesListModelSerializer(ModelSerializer):
    class Meta:
        model = Images
        exclude = ()


class ImagesUpdateModelSerializer(ModelSerializer):

    def get_validators(self):
        if Images.objects.filter(id=self.instance.id).exists():
            return super().get_validators()
        return ValidationError('Object not found', 404)

    def update(self, instance, validated_data):
        old_image = instance.image.file.name
        new_image = validated_data['image']
        if has_difference_images(old_image, new_image):
            # Delete old photo
            delete_main_photo(Images, instance.id)
            return super().update(instance, validated_data)
        # if hasn't differences between images
        return Images.objects.get(id=instance.id)

    class Meta:
        model = Images
        exclude = ('object_id', 'content_type')


class RatingModelSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ()


class CommentsModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['user'] = GetUserNameSerializer(instance.user).data
        return represent

    class Meta:
        model = Comments
        exclude = ('slug',)


class CommentsListModelSerializer(ModelSerializer):
    class Meta:
        model = Comments
        exclude = ()


class SalesModelSerializer(ModelSerializer):
    class Meta:
        model = Sales
        exclude = ()


class BasketModelSerializer(ModelSerializer):
    class Meta:
        model = Basket
        exclude = ()


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class PaymentsModelSerializer(ModelSerializer):
    class Meta:
        model = Payments
        exclude = ()
