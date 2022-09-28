from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Packages


@registry.register_document
class PackagesDocument(Document):
    class Index:
        name = 'packages'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Packages
        fields = [
            'title',
            'link',
            'guid',
            'description',
            'author',
            'pubDate',
        ]
