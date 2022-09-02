from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# class Type(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


class CompanyForCPU(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=30, null=True)
    logo = models.ImageField(upload_to='publisher-logo', null=True)

    def __str__(self):
        return self.name

#CentralProcessingUnit
class CPU(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    company = models.ForeignKey(CompanyForCPU, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='CSP-images', null=True)
    created_date = models.DateTimeField(auto_now=True)
    #type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
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
    count = models.IntegerField(default=0)



    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class CPUImages(models.Model):
    image = models.ImageField(upload_to='CSP-images/CPU-images')
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)


class CPURating(models.Model):
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)

    def __init__(self):
        return f"{self.user} {self.cpu} {self.rating}"


class CPUComments(models.Model):
    text = models.TextField(default='', max_length=500, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return f"{self.cpu} {self.user} {self.text} {self.created_date}"


class CPUParty(models.Model):
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cpu} {self.price} {self.count} {self.created_date}"


class SalesForCpu(models.Model):
    percent = models.FloatField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user}"


class Basket(models.Model):
    #{'model': 'CPU', 'id': 22}
    computer_spare_part = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.computersparepart} {self.user} {self.count}"


class Order(models.Model):
    computersparepart = models.ForeignKey(СomputerSparePart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    #status
    # 1-ordered
    # 2-paid
    # 3-delevired
    # 4-received
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.computersparepart} {self.user} {self.count} {self.status}"


class PaymentType(models.Model):
    # 1-credit card
    name = models.CharField(max_length=60)


class Payments(models.Model):
    computersparepart = models.ForeignKey(СomputerSparePart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.computersparepart} {self.user} {self.amount}"