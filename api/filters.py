import django_filters

from api.models import Titles, Genres, Categories


class ModelFilter(django_filters.FilterSet):
    genre = django_filters.ModelChoiceFilter(field_name='genre__slug',
                                             to_field_name='slug',
                                             queryset=Genres.objects.all())

    category = django_filters.ModelChoiceFilter(field_name='category__slug',
                                                to_field_name='slug',
                                                queryset=Categories.objects.all())

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Titles
        fields = ('genre', 'category', 'year', 'name')
