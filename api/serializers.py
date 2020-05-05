from rest_framework import serializers

from .models import User, Categories, Review, Comments


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


class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'role', 'email', 'first_name', 'last_name', 'bio']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date']


class CommentsSerializer(serializers.ModelSerializer):
    model = Comments
    fields = ['id', 'text', 'author', 'pub_date']
