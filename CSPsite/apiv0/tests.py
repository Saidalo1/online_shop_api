from django.test import TestCase
from .models import *
# Create your tests here.

class TypeTestCase(TestCase):
    def setUp(self):
        self.type = Type.objects.create(name="Prootsessor")

    def test_type_count_and_create(self):
        type = Type.objects.all()
        self.assertEqual(len(type), 1)
        self.assertEqual(self.type, type[0])
    
    def test_update_type(self):
        self.type.name = "Bunyodkor"
        self.type.save()

        type = Type.objects.first()
        self.assertEqual(self.type, type)
    
    def test_delete(self):
        self.type.delete()

        type = Type.objects.all()
        self.assertEqual(len(type), 0)


class CompanyTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="AMDD", city="Tashkent", email='newboy.secret@mail.ru')

    def test_company_count_and_create(self):
        company = Company.objects.all()
        self.assertEqual(len(company), 1)
        self.assertEqual(self.company, company[0])
    
    def test_update_company(self):
        self.company.name = "Bunyodkor"
        self.company.city = "Toshkent"
        self.email = "super.saydalo@mail.ru"
        self.company.save()

        company = Company.objects.first()
        self.assertEqual(self.company, company)
    
    def test_delete(self):
        self.company.delete()

        company = Company.objects.all()
        self.assertEqual(len(company), 0)


class ComputerSparePartTestCase(TestCase):
    def setUp(self):
        type = Type.objects.create(name="Prootsessor")
        company = Company.objects.create(name="AMDD", city="Tashkent", email='111')

        self.computersparepart = ComputerSparePart.objects.create(
            name = "Intel",
            description = "zor",
            company = company,
            type = type,
            cores = 16,
            flow = "24",
            ghz = "5.2",
            processor_series = '',
            graphics_processing_unit = '',
            graphics_processing_unit_frequency = '',
            video_memory_type = '',
            count = "59",
        )

    def test_computersparepart_count_and_create(self):
        computersparepart = ComputerSparePart.objects.all()
        self.assertEqual(len(computersparepart), 1)
        self.assertEqual(self.computersparepart, computersparepart[0])
    
    def test_update_computersparepart(self):
        self.computersparepart.name = "AMD"
        self.computersparepart.save()

        computersparepart = ComputerSparePart.objects.first()
        self.assertEqual(self.computersparepart, computersparepart)
    
    def test_delete(self):
        self.computersparepart.delete()

        computersparepart = ComputerSparePart.objects.all()
        self.assertEqual(len(computersparepart), 0)


class ClientsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="User", password="123321")
        self.client = Clients.objects.create(user=user, phone_number='+998798442753')

    def test_client_count_and_create(self):
        client = Clients.objects.all()
        self.assertEqual(len(client), 1)
        self.assertEqual(self.client, client[0])
    
    def test_update_client(self):
        self.client.phone_number = "+998998442753"
        self.client.save()

        client = Clients.objects.first()
        self.assertEqual(self.client, client)
    
    def test_delete(self):
        self.client.delete()

        client = Clients.objects.all()
        self.assertEqual(len(client), 0)


class RatingTestCase(TestCase):
    def setUp(self):
        type = Type.objects.create(name="Prootsessor")
        company = Company.objects.create(name="AMDD", city="Tashkent", email='111')
        computersparepart = ComputerSparePart.objects.create(
            name = "Intel",
            description = "zor",
            company = company,
            type = type,
            cores = 16,
            flow = "24",
            ghz = "5.2",
            processor_series = '',
            graphics_processing_unit = '',
            graphics_processing_unit_frequency = '',
            video_memory_type = '',
            count = "59",
        )
        user = User.objects.create(username="User", password="123321")
        
        self.rating = Rating.objects.create(user=user, computer_spare_part=computersparepart, rating = 1)

    def test_rating_count_and_create(self):
        rating = Rating.objects.all()
        self.assertEqual(len(rating), 1)
        self.assertEqual(self.rating, rating[0])
    
    def test_update_rating(self):
        self.rating.rating = "5"
        self.rating.save()

        rating = Rating.objects.first()
        self.assertEqual(self.rating, rating)
    
    def test_delete(self):
        self.rating.delete()

        rating = Rating.objects.all()
        self.assertEqual(len(rating), 0)


# class CommentsTestCase(TestCase):
#     def setUp(self):
#         user = User.objects.create(username="User", password="123321")
#         self.comment = Comments.objects.create(user=user, phone_number='+998798442753')

#     def test_comment_count_and_create(self):
#         comment = Comments.objects.all()
#         self.assertEqual(len(comment), 1)
#         self.assertEqual(self.comment, comment[0])
    
#     def test_update_comment(self):
#         self.comment.phone_number = "+998998442753"
#         self.comment.save()

#         comment = Comments.objects.first()
#         self.assertEqual(self.comment, comment)
    
#     def test_delete(self):
#         self.comment.delete()

#         comment = Comments.objects.all()
#         self.assertEqual(len(comment), 0)
