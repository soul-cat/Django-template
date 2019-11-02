from rest_framework import routers
from .views import *

router_novel = routers.DefaultRouter()

router_novel.register('noveluser', NovelUserViewSet)
router_novel.register('menu', MenuViewSet)
router_novel.register('novel', NovelViewSet)
router_novel.register('comment', CommentViewSet)
router_novel.register('carousel', CarouselViewSet)
