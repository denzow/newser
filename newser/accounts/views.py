# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {
        "user": request.user
    }
    return render(request, "accounts/profile.html", context=context)
