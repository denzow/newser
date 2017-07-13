from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=1000)
    url = models.URLField(max_length=2000)

    def __str__(self):
        return "{}".format(self.title)

