from django.db import models
from django.contrib.auth.models import AbstractUser


class SiteUsers(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    email = models.EmailField(verbose_name='почта', unique=True, blank=True)
