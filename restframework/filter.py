import django_filters
from .models import *


class AuthorFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Author
        fields = ['name']