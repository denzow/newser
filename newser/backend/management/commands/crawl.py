from django.core.management.base import BaseCommand
from backend.crawlers import FeedsCrawler


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('all')

    def handle(self, *args, **options):
        is_all = options['all']
        if is_all:
            FeedsCrawler().run(is_all=True)
        else:
            FeedsCrawler().run(is_all=True)
