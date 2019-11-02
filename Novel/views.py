from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rest_framework import viewsets
from Novel.filter import *
from validateimg import image
from random import sample
from string import ascii_lowercase, ascii_uppercase, digits
from Novel.serializers import *

# Create your views here.


def creat_code_img(request):
    img = image.ImageCaptcha()
    code = sample(ascii_lowercase + ascii_uppercase + digits, 4)
    code = ''.join(code)
    date = img.generate(code)
    request.session['code'] = code
    return HttpResponse(date, 'image/png')


def go_login(request):
    context = {}
    username = request.get_signed_cookie('username', default='')
    context['username'] = username
    context['password'] = '123'
    return render(request, 'Novels/novel_login.html', context=context)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    if str(request.POST['code']).lower() == str(request.session['code']).lower():
        if username == 'fan' and password == '123':
            red = HttpResponseRedirect('/Novel/homepage')
            red.set_signed_cookie(key='username', value=username, max_age=3600)
            request.session['login_state'] = True
            if request.POST.getlist('true'):
                red.set_signed_cookie('password', password, max_age=3600)
            return red
        else:
            request.session['login_state'] = False
            red = HttpResponseRedirect('/Novel/go_login')
            return red
    else:
        red = HttpResponseRedirect('/Novel/go_login')
        request.session['login_state'] = False
        return red


def go_register(request):
    red = render(request, 'Novels/novel_register.html')
    return red


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    name = request.POST['name']
    email = request.POST['email']
    ob = NovelUser.objects.filter(pen_name=username)
    if len(ob) != 0:
        return HttpResponse('笔名已存在')
    else:
        NovelUser.objects.create(
            pen_name=username,
            password=password,
            name=name,
            email=email
        )
        return HttpResponse('注册成功')


def homepage(request):
    return render(request, 'Novels/HomePage.html')


def training(request):
    username = request.GET['username']
    ob = NovelUser.objects.filter(pen_name=username)
    if len(ob) == 0:
        return HttpResponse('true')
    else:
        return HttpResponse('false')


class User(View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')


class NovelUserViewSet(viewsets.ModelViewSet):
    queryset = NovelUser.objects.all()
    serializer_class = NovelUserSerializers
    filter_class = NovelUserFilter


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class NovelViewSet(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializers
    filter_class = NovelFilter


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializers
