import feedparser
from .models import Articles, RssFeeds
from dateutil.parser import parser


class FeedsCrawler(object):
    """
    Feedをいい感じにする
    """

    def __init__(self):
        self.feed_list = RssFeeds.objects.all()

    def run(self):
        """
        登録済みFeedについてすべて取得する
        :return:
        """
        for feed in self.feed_list:
            print(feed.get_max_timestamp())
            feed_result = feedparser.parse(feed.url, modified=feed.get_max_timestamp())
            #feed_result = feedparser.parse(feed.url)
            for entry in feed_result.entries:
                print(entry.title)
                update_time_str = entry.updated
                new_article = Articles()
                new_article.url = entry.link
                new_article.title = entry.title
                new_article.summary = entry.summary
                new_article.timestamp = parser().parse(timestr=update_time_str)
                new_article.source = feed
                new_article.save()

