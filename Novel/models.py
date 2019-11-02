from django.db import models
from django.utils import timezone

# Create your models here.


class NovelUser(models.Model):
    pen_name = models.CharField(max_length=16, verbose_name='笔名/用户名')
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=12, verbose_name='真实姓名')
    email = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name = '用户表'


class Menu(models.Model):
    title = models.CharField(max_length=20, verbose_name='小说分类')

    class Meta:
        verbose_name = '标题表'


class Novel(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    content = models.TextField(max_length=65530, verbose_name='正文')
    create_time = models.DateTimeField(verbose_name='创作时间', default=timezone.now)
    read_times = models.IntegerField(verbose_name='阅读次数', default=0)
    level = models.IntegerField(verbose_name='小说等级，对2求余分5等')
    novel_user = models.ForeignKey(NovelUser, on_delete=models.CASCADE, verbose_name='关联用户')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='关联大分类标题')

    class Meta:
        verbose_name = '小说表'


class Comment(models.Model):
    content = models.CharField(max_length=200, verbose_name='评论内容')
    novel_user = models.ForeignKey(NovelUser, on_delete=models.CASCADE, verbose_name='关联用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='关联小说', default=None)

    class Meta:
        verbose_name = '评论表'


class Carousel(models.Model):
    content = models.CharField(max_length=20, verbose_name='滚动字幕')
    color = models.CharField(max_length=20, verbose_name='字体颜色')

    class Meta:
        verbose_name = '轮播表'
