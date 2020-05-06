from rest_framework import serializers

from .models import User, Categories, Genre, Title, Comments, Review


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


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    def validate_score(self, value):
        if 0 < value <= 10:
            return value
        raise serializers.ValidationError('Оценка должна быть от 1 до 10.')

    def validate(self, data):
        title_id = self.context['view'].kwargs.get('title_id')
        user = self.context['request'].user
        is_review_exist = Review.objects.filter(title=title_id, author=user).exists()
        if is_review_exist:
            raise serializers.ValidationError('Вы уже оставили отзыв.')
        return data

    class Meta:
        model = Review
        fields = ['id', 'pub_date', 'author', 'text', 'score']
        #  read_only_fields = ['id', 'pub_date', 'author']


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text', 'author', 'pub_date']
        #  read_only_fields = ['id', 'pub_date', 'author']
