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


class Category(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.TextField(max_length=50)
    year = models.IntegerField("Год выпуска")
    description = models.TextField(max_length=200, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="category_titles", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_review")
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    score = models.IntegerField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="title_review")
    rating = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comments")
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_comments")

    def __str__(self):
        return self.text
