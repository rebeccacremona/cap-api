import django_filters
from .models import Case, Jurisdiction


class CaseFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    name_abbreviation = django_filters.CharFilter(name="slug", lookup_expr='icontains')
    citation = django_filters.CharFilter(name="citation", lookup_expr='icontains')
    court_name = django_filters.CharFilter(name="court__name", lookup_expr='icontains')
    reporter_name = django_filters.CharFilter(name="reporter__name", lookup_expr='icontains')
    min_year = django_filters.DateTimeFilter(name="decisiondate", lookup_expr='gte')
    max_year = django_filters.DateTimeFilter(name="decisiondate", lookup_expr='lte')
    reporter_name = django_filters.CharFilter(name="reporter__name", lookup_expr='icontains')
    jurisdiction_name = django_filters.CharFilter(name="jurisdiction__name", lookup_expr='icontains')

    class Meta:
        model = Case
        fields = ['name', 'name_abbreviation', 'citation',
                  'jurisdiction', 'court_name', 'reporter_name',
                  'min_year', 'max_year']


class JurisdictionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Jurisdiction
        fields = '__all__'
