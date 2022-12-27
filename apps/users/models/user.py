from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField


class User(AbstractUser):
    phone = CharField(max_length=12, null=True, blank=True)
    is_active = BooleanField(default=False)

    REQUIRED_FIELDS = ['phone', 'email']
