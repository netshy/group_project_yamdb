from rest_framework import serializers

from .models import User, Categories, Genres, Title


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


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name', 'slug',)


class TitleSlugSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, slug_field='slug', queryset=Genres.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Categories.objects.all())

    class Meta:
        model = Title
        fields = '__all__'


class TitleGeneralSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()

    class Meta:
        model = Title
        fields = '__all__'



class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'role', 'email', 'first_name', 'last_name', 'bio']
