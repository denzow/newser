import feedparser
from .models import Articles, RssFeeds
from dateutil.parser import parser
from bs4 import BeautifulSoup
import requests
import base64

class FeedsCrawler(object):
    """
    Feedをいい感じにする
    """

    def __init__(self):
        self.feed_list = RssFeeds.objects.all()

    def run(self, is_all=False):
        """
        登録済みFeedについてすべて取得する
        :return:
        """

        for feed in self.feed_list:
            print(feed.get_max_timestamp())
            if is_all:
                feed_result = feedparser.parse(feed.url)
            else:
                feed_result = feedparser.parse(feed.url, modified=feed.get_max_timestamp())
            #feed_result = feedparser.parse(feed.url)
            images_buffer = []
            for i, entry in enumerate(feed_result.entries):
                print(entry.title)
                update_time_str = entry.updated
                new_article = Articles()
                new_article.url = entry.link
                new_article.title = entry.title
                new_article.summary = entry.summary
                new_article.timestamp = parser().parse(timestr=update_time_str)
                new_article.source = feed

                res = requests.get(entry.link)
                soup = BeautifulSoup(res.content, "html.parser")
                if i == 0:
                    for img in soup.select("img"):
                        images_buffer.append(img.get("src"))
                try:
                    for img in soup.select("img"):
                        #print(img.get("src"))
                        if img.get("src") not in images_buffer:
                            response = requests.get(img.get("src"))
                            uri = ("data:" +
                                   response.headers['Content-Type'] + ";" +
                                   "base64," + base64.b64encode(response.content).decode("utf-8"))
                            #print(uri)
                            new_article.thumbnail = uri
                            break
                except Exception as ex:
                    # TODO
                    pass
                new_article.save()
