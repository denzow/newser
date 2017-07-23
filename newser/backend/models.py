from django.db import models
from django.utils.timezone import now, utc



class RssFeeds(models.Model):

    url = models.URLField(max_length=2000)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.name)


class Articles(models.Model):

    url = models.URLField(max_length=2000, primary_key=True)
    # base64
    thumbnail = models.CharField(max_length=20000, default=None, null=True)
    title = models.CharField(max_length=1000)
    summary = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(default=now)
    source = models.ForeignKey(RssFeeds, name="source", default=None, null=True)

    def __str__(self):
        return "{}".format(self.title)

