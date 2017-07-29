from django.db import models
from django.utils.timezone import now, utc



class RssFeeds(models.Model):

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
        return self.related_articles.aggregate(models.Max('timestamp'))["timestamp__max"]


class Articles(models.Model):

    url = models.URLField(max_length=2000, primary_key=True)
    # base64
    thumbnail = models.CharField(max_length=20000, default=None, null=True)
    title = models.CharField(max_length=1000)
    summary = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=now)
    source = models.ForeignKey(RssFeeds, name="source", related_name="related_articles", default=None, null=True)

    def __str__(self):
        return "{}".format(self.title)

