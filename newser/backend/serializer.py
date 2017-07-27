from rest_framework import serializers

from .models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source="source.name")

    class Meta:
        model = Articles
        fields = ('title', 'url', "summary", "timestamp", "source_name", "thumbnail")

