from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.USER)
    bio = models.TextField(max_length=200, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Genres(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.TextField(max_length=50)
    year = models.IntegerField("Год выпуска")
    description = models.TextField(max_length=200)
    genre = models.ManyToManyField(Genres)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, related_name="category_titles", null=True, blank=True
    )

    def __str__(self):
        return self.name

