from django.contrib import admin
from .models import User, Categories, Genres, Title
# Register your models here.

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Title)