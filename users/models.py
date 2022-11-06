from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    photo = models.ImageField(
        null=True,
    )
