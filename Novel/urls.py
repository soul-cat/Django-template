#专门声明当前应用的url与视图的映射关系
from django.urls import path
from .views import *
urlpatterns = [

    path('create_code', creat_code_img, name='code'),
    path('login', login, name='login'),
    path('homepage', homepage),
    path('go_login', go_login),
    path('go_register', go_register),
    path('register', register),
    path('user', User.as_view())

]