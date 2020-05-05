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
    slug = models.SlugField()

    def __str__(self):
        return self.slug


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)


# Максим, надо сослаться на модель, чтобы при удалении произведения, удалялся отзыв
class Review(models.Model):
    author = models. ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    score = models.PositiveIntegerField()
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comment_obj')


