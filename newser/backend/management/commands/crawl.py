from django.core.management.base import BaseCommand
from backend.crawlers import FeedsCrawler


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--all", action='store_true', dest='is_all', default=False)

    def handle(self, *args, **options):
        is_all = options['is_all']
        if is_all:
            print("all mode")
            FeedsCrawler().run(is_all=True)
        else:
            FeedsCrawler().run(is_all=True)
