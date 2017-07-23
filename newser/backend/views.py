from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from .models import Articles
from .serializer import ArticleSerializer
from .logics import FeedsCrawler
# Create your views here.


def test(request):
    context = {
        "user": "DEMO"
    }
    return render(request, "accounts/profile.html", context=context)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # ログイン済みでなければ全件戻す
        #FeedsCrawler().run()
        if self.request.user.id:
            # TODO
            return Articles.objects.all().order_by("-timestamp")
        else:
            return Articles.objects.all().order_by("-timestamp")

