from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        null=True,
        max_length=50
    )
    slug = models.SlugField(
        null=True,
    )

    def __str__(self):
        return self.name


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
    image = models.ImageField(
        null=True,
        upload_to='post_images/%y/%m/%d'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
    )
    # author = models.ForeignKey(
    #     'users.BlogUser',
    #     on_delete=models.CASCADE,
    #     null=True,
    # )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'posts_by_author',
            kwargs={'pk': self.id}
        )
