import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.USER)
    bio = models.TextField(max_length=200, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(max_length=50)
    year = models.IntegerField("Год выпуска")
    description = models.TextField(max_length=200)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, related_name="genre_titles", null=True, blank=True
    )
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, related_name="category_titles", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_review")
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    score = models.IntegerField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="title_review")


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comments")
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_comments")
