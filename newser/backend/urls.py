from rest_framework import routers
from .views import ArticleViewSet


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name="article")
