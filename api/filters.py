import django_filters

from .models import Title, Genre, Categories


class ModelFilter(django_filters.FilterSet):
    genre = django_filters.ModelChoiceFilter(
        field_name='genre__slug',
        to_field_name='slug',
        queryset=Genre.objects.all())

    category = django_filters.ModelChoiceFilter(
        field_name='category__slug',
        to_field_name='slug',
        queryset=Categories.objects.all())

    name = django_filters.CharFilter(field_name='name', method='test')

    def test(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

    class Meta:
        model = Title
        fields = ('genre', 'category', 'year', 'name')
