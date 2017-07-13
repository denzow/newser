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


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

