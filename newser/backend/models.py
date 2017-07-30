from django.db import models
from django.utils.timezone import now, utc
from django.conf import settings

class RssFeeds(models.Model):
    """
    RSS Feeds
    """

    url = models.URLField(max_length=2000)
    name = models.CharField(max_length=1000)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return "{}:{}".format(self.name, self.valid)

    @classmethod
    def get_valid_feeds(cls):
        """
        フィードの一覧について有効になっているものだけ戻す
        :return:
        """
        return cls.objects.filter(valid=True)

    def get_max_timestamp(self):
        """
        関連フィードの最大の更新時間
        :return:
        """
        return self.related_articles.aggregate(models.Max('timestamp'))["timestamp__max"]


class Articles(models.Model):
    """
    記事
    """

    url = models.URLField(max_length=2000, primary_key=True)
    # base64
    thumbnail = models.CharField(max_length=20000, default=None, null=True)
    title = models.CharField(max_length=1000)
    summary = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=now)
    source = models.ForeignKey(RssFeeds, name="source", related_name="related_articles", default=None, null=True)

    def __str__(self):
        return "({}){}".format(self.source, self.title)


class ReadHistories(models.Model):
    """
    読み込み履歴
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="red_article", on_delete=models.CASCADE,)
    article = models.ForeignKey(Articles, name="red_article")
    timestamp = models.DateTimeField(default=now)

