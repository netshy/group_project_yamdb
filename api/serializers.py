from rest_framework import serializers

from .models import User, Categories, Genre, Title


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'role', 'email', 'first_name', 'last_name', 'bio']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class TitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='genre.slug'
    )
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='category.slug'
    )

    class Meta:
        model = Title
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'role', 'email', 'first_name', 'last_name', 'bio']
