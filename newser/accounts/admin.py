# coding:utf-8

# Register your models here.
from django.contrib import admin
from accounts.models import CustomUser

admin.site.register(CustomUser)