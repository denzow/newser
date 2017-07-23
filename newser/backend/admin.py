from django.contrib import admin

from .models import Articles, RssFeeds


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(RssFeeds)
class RssFeedAdmin(admin.ModelAdmin):
    pass