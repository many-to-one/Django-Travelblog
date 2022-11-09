from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from posts.models import Post


class BlogUser(AbstractUser):
    photo = models.ImageField(
        null=True,
        upload_to='photo/%Y/%m/%d'
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_director = models.BooleanField(
        default=False,
    )
    posts = models.ManyToManyField(
        Post,
    )

    REQUIRED_FIELDS =['email']
    
    def get_absolute_url(self):
        return reverse(
            'profile_view',
            kwargs={'pk': self.id}
        )
