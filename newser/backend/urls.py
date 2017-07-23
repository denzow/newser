from django.conf.urls import url
from rest_framework import routers
from .views import ArticleViewSet, test


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name="article")
urlpatterns = [
    url(r'^test/$', test),
]
urlpatterns += router.urls