from rest_framework import routers
from restframework import views
# 获取路由器对象
router = routers.DefaultRouter()
# 向路由器对象中注册视图
# 参数1资源名(rest风格里资源就是终点，就url最后一部分)
# 参数2为视图集
router.register('author', views.AuthorViewSet)
router.register('blog', views.BlogViewSet)