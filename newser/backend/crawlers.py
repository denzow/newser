import feedparser
from .models import Articles, RssFeeds
from dateutil.parser import parser
from bs4 import BeautifulSoup
import requests
import base64
from urllib.parse import urljoin
from logging import getLogger
logger = getLogger(__name__)


class FeedsCrawler(object):
    """
    Feedをいい感じにする
    """

    def __init__(self):
        self.feed_list = RssFeeds.get_valid_feeds()

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
            first_article_buffer = None
            for i, entry in enumerate(feed_result.entries):
                print(entry.title)
                res = requests.get(entry.link)
                update_time_str = entry.updated
                new_article = Articles()
                new_article.url = res.url
                new_article.title = entry.title
                new_article.summary = entry.summary
                new_article.timestamp = parser().parse(timestr=update_time_str)
                new_article.source = feed

                soup = BeautifulSoup(res.content, "html.parser")
                # 1記事目は画像リストだけとっておく。実際の保存は2記事目後
                if i == 0:
                    images_buffer = self._get_all_image_urls(soup)
                    first_article_buffer = (soup, new_article)
                    continue

                try:
                    article_image_url_list = self._get_all_image_urls(soup)
                    for img_src in article_image_url_list:
                        if img_src not in images_buffer:
                            new_article.thumbnail = self._image_to_base64(img_src, new_article.url)
                            break

                except IndentationError as ex:
                    print(ex)

                    pass
                new_article.save()

                # 最初の記事で固有の画像がわかるのは2記事目を見た後
                if i == 1:
                    images_buffer = self._get_all_image_urls(soup)
                    for img_src in self._get_all_image_urls(first_article_buffer[0]):
                        if img_src not in images_buffer:
                            first_article_buffer[1].thumbnail = self._image_to_base64(img_src, first_article_buffer[1].url)
                            first_article_buffer[1].save()
                            break


    @staticmethod
    def _get_all_image_urls(soup: BeautifulSoup):
        images_buffer = []
        for img in soup.select("img"):
            images_buffer.append(img.get("src"))
        return images_buffer

    @staticmethod
    def _image_to_base64(image_url: str, article_url: str):
        if not image_url.startswith("http://") or not image_url.startswith("https://"):
            image_url = urljoin(article_url, image_url)
        response = requests.get(image_url)
        uri = ("data:" +
               response.headers['Content-Type'] + ";" +
               "base64," + base64.b64encode(response.content).decode("utf-8"))
        return uri
