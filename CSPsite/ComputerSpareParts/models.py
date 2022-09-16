from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=30, null=True)
    logo = models.ImageField(upload_to='publisher-logo', null=True)
    # type = models.ForeignKey(Type, null=False)

    def __str__(self): 
        return self.name


class ComputerSparePart(models.Model):
    name = models.CharField(max_length=80, null=False)
    description = models.CharField(max_length=1000, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='CSP-images', null=True)
    created_date = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    #rating = models.ForeignKey(Rating, on_delete=models.PROTECT)
    #sale = models.BooleanField(Sales, default=False)
    сores = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(1)
        ])
    flow = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(256),
            MinValueValidator(0)
        ])
    ghz = models.FloatField(default=0,
        validators=[
            MaxValueValidator(8.429),
            MinValueValidator(0)
        ])
    processor_series = models.CharField(max_length=300, null=True)#для видеокарты (пока что CharField)
    graphics_processing_unit = models.CharField(max_length=300, null=True)#для видеокарты (пока что CharField)
    graphics_processing_unit_frequency = models.CharField(max_length=300, null=True)#для видеокарты (пока что CharField)
    video_memory_type = models.CharField(max_length=300, null=True)#для видеокарты (пока что CharField)
    count = models.IntegerField(default=0)



    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Images(models.Model):
    image = models.ImageField(upload_to='CSP-images')
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)

    def __init__(self):
        return f"{self.user} {self.computer_spare_part} {self.rating}"


class Comments(models.Model):
    text = models.TextField(default='', max_length=500, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return f"{self.computer_spare_part} {self.user} {self.text} {self.created_date}"


class Party(models.Model):
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.computer_spare_part} {self.price} {self.count} {self.created_date}"


class Sales(models.Model):
    percent = models.FloatField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.percent} {self.description} {self.from_date} {self.to_date}"


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user}"


class Basket(models.Model):
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.computer_spare_part} {self.user} {self.count}"


class Order(models.Model):
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    #status
    # 1-ordered
    # 2-paid
    # 3-delevired
    # 4-received
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.computer_spare_part} {self.user} {self.count} {self.status}"


class PaymentType(models.Model):
    # 1-credit card
    name = models.CharField(max_length=60)


class Payments(models.Model):
    computer_spare_part = models.ForeignKey(ComputerSparePart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.computer_spare_part} {self.user} {self.amount}"