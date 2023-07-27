from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
  email = models.EmailField(unique=True)
  code = models.CharField(max_length=255, null=True, blank=True)
  access_level = models.IntegerField(null=True, blank=True)
  phone_number = models.CharField(max_length=255, null=True, blank=True)
  address = models.TextField(null=True, blank=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
