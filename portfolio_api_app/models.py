from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from portfolio_api_project import settings

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile_number']

    def __str__(self):
        return self.email


class Portfolio(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='portfolio',
        null=True,
        blank=True
    )
    role = models.CharField(max_length=50)
    introduction = models.CharField(max_length=1000)


class WorkExperince(models.Model):
    user = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='work_experiences'
    )
    occupation_title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    tags = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.occupation_title


class Language(models.Model):
    user = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='languages'
    )
    language = models.JSONField(default=list, blank=True, null=True)
    level = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.language
