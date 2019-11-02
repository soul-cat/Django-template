from rest_framework import serializers
from .models import *
from Novel.serializers import *


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    # blog_set = serializers.CharField()
    author = serializers.CharField(source='author.name')

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']
        # depth = 1
        extra_kwargs = {'title': {'max_length': 2}}


class AuthorSerializer(serializers.ModelSerializer):
    # blog_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())
    # blog_set = BlogSerializer(many=True, read_only=True)

    class Meta:
        # 需要进行序列化的模型类
        model = Author
        # 定义了序列化/反序列化的字段
        fields = ['id', 'name', 'age']
        # depth = 1
