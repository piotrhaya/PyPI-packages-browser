from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Packages
from .documents import PackagesDocument


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = [
            'title',
            'link',
            'guid',
            'description',
            'author',
            'pubDate'
        ]


class PackagesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PackagesDocument
        fields = [
            'title',
            'link',
            'guid',
            'description',
            'author',
            'pubDate'
        ]
