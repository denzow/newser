from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from .models import Articles
from .serializer import ArticleSerializer

# Create your views here.


def index(request):
    context = {
        "user": "DEMO"
    }
    return render(request, "accounts/profile.html", context=context)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # ログイン済みでなければ全件戻す
        if self.request.user.id:
            # TODO
            return Articles.objects.all()
        else:
            return Articles.objects.all()

