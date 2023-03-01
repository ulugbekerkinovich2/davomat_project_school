from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext as _

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError(_('Iltimos, foydalanuvchi nomini kiriting'))

        # username_validator = UnicodeUsernameValidator(min_length=5)
        # username_validator(username)
        # if len(username) < 5:
        #     raise ValueError(_('Ism 5 ta belgidan kam bo\'lmasligi kerak'))
        # if len(password) < 8:
        #     raise ValueError(_('Parol 8 ta belgidan kam bo\'lmasligi kerak'))
        if password:
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, username, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Name'), max_length=50, unique=True)
    # user_phone = models.CharField(_('Phone Number'), max_length=20,
    #                               unique=True, default=None, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


def __str__(self):
    return f'{self.username}'


class Student(models.Model):
    full_name = models.CharField(max_length=60, null=False, unique=True)

    def save(self, *args, **kwargs):
        self.full_name = self.full_name.lower()
        super(Student, self).save(*args, **kwargs)
