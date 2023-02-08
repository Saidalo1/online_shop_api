from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, EmailField
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        if User.objects.filter(email=email).exists():
            raise ValueError("This email is already exists")
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = EmailField(_("email address"))
    phone = CharField(max_length=12, null=True, blank=True)
    is_active = BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ('email',)
