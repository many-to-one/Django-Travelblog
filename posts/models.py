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
    image_header = models.ImageField(
        null=True,
        upload_to=('categories/%Y/%m/%d')
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            'posts_by_category',
            kwargs={'pk': str(self.id)}
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
    views = models.IntegerField(
        default=0,
    )
    likes = models.ManyToManyField(
        BlogUser,
        default=0,
        # related_name is important here for relationship, because of author
        related_name='likes',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'post_view',
            kwargs={
                'pk': self.id,
                'cpk': self.category.id,
                'apk': self.author.id,
            }
        )

    def get_views(self, *args, **kwargs):
        self.views += 1
        super().save(*args, **kwargs)
        return self.views

    def get_likes(self):

        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
    )
    body = models.TextField(
        max_length=500,
        null=True,
    )
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.post}: {self.body}'