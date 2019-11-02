import django_filters
from .models import *


class NovelUserFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = NovelUser
        fields = ['name', 'pen_name']


class NovelFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Novel
        fields = ['title', 'menu']