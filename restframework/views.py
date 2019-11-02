from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import *
from .pagenation import *
from .filter import *

# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ['name', 'age']
    filter_class = AuthorFilter


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
