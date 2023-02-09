# import pytest
# from django.db.utils import IntegrityError
# from faker import Faker
# from model_bakery import baker
#
# from orders.models import ProductImages, Product
#
#
# @pytest.mark.django_db
# class TestProductImagesView:
#
#     @pytest.fixture
#     def product(self):
#         return baker.make()
#
#     @pytest.fixture
#     def product_image(self):
#         return baker.make(ProductImages, product=, image=Faker.file_path(category='image'))
#
#     @pytest.fixture
#     def companies(self):
#         faker = Faker()
#         baker.make(ProductImages, _quantity=10, name=faker.text()[:50])
#
#     def test_create_product_image_model(self, companies):
#         product_image = ProductImages.objects.create(name='New ProductImages')
#         count = ProductImages.objects.count()
#         assert count == 11
#         assert product_image.name == 'New ProductImages'
#
#         # wrong test
#         try:
#             ProductImages.objects.create(name=None)
#             assert False
#         except IntegrityError:
#             assert True
#
#     def test_update_product_image_model(self, product_image):
#         name = 'NEW NAME'
#         product_image.name = name
#         product_image.save()
#         assert product_image.name == name
#
#         # wrong test
#         try:
#             product_image.name = None
#             product_image.save()
#             assert False
#         except IntegrityError:
#             assert True
#
#     def test_delete_product_image_model(self, product_image):
#         old_count = ProductImages.objects.count()
#         assert old_count == 1
#         product_image.delete()
#         new_count = ProductImages.objects.count()
#         assert new_count == 0
