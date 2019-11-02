from rest_framework import serializers
from Novel.models import *


class NovelUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = NovelUser
        fields = '__all__'


class NovelSerializers(serializers.ModelSerializer):
    novel_user = serializers.CharField(source='novel_user.name')
    menu = serializers.CharField(source='menu.title')

    class Meta:
        model = Novel
        fields = '__all__'


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = '__all__'
