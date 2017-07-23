from django.db import models


class Articles(models.Model):

    url = models.URLField(max_length=2000)
    title = models.CharField(max_length=1000)
    summary = models.CharField(max_length=2000)

    def __str__(self):
        return "{}".format(self.title)

