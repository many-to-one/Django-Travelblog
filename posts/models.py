from django.db import models
from django.urls import reverse

from users.models import BlogUser


class Category(models.Model):
    name = models.CharField(
        null=True,
        max_length=50
    )
    slug = models.SlugField(
        null=True,
    )
    snippet = models.TextField(
        null=True,
        max_length=200,
    )
    image = models.ImageField(
        null=True,
        upload_to=('categories/%Y/%m/%d')
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'posts_by_category',
            kwargs={'slug': self.slug}
        )


class Post(models.Model):
    title = models.CharField(
        null=True,
        max_length=50
    )
    slug = models.SlugField(
        null=True,
    )
    body = models.TextField(
        null=True,
    )
    snippet = models.TextField(
        null=True,
        max_length=200,
    )
    image = models.ImageField(
        null=True,
        upload_to='post_images/%Y/%m/%d'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
    )
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'post_view',
            kwargs={'pk': self.id}
        )
