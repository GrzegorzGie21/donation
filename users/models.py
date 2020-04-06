from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    # username = None
    email = models.EmailField(_('email_address'), unique=True)
    city = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

