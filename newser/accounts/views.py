# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    print(dir(request.user))
    return HttpResponse("Hello, world. You're at the polls index. you are {}".format(request.user.username))
