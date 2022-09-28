from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FunctionalSuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from django_elasticsearch_dsl_drf.constants import (
    FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
    FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
)

from .serializers import PackagesSerializer, PackagesDocumentSerializer
from .documents import PackagesDocument

from django.shortcuts import render


class PackagesSearchWithViewSet(DocumentViewSet):
    document = PackagesDocument
    serializer_class = PackagesDocumentSerializer
    filter_backends = [SearchFilterBackend, FunctionalSuggesterFilterBackend]

    search_fields = [
        'title',
        'link',
        'guid',
        'description',
        'author',
        'pubDate'
    ]
    filter_fields = {
        'title': 'title',
        'link': 'link',
        'guid': 'guid',
        'description': 'description',
        'author': 'author',
        'pubDate': 'pubDate'
    }

    functional_suggester_fields = {
        'title_suggest': {
            'field': 'title.raw',
            'suggesters': [
                FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
            ],
            'default_suggester': FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
            'options': {
                'size': 25,
                'from': 0,
            }
        },
        'title_suggest_match': {
            'field': 'title.edge_ngram_completion',
            'suggesters': [FUNCTIONAL_SUGGESTER_COMPLETION_MATCH],
            'default_suggester': FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
        }
    }


def search(request):
    q = request.GET.get('q')

    if q:
        packages = PackagesDocument.search().query("multi_match", query=q, fields=['title', 'description', 'author'])
    else:
        packages = ''
    return render(request, 'search.html', {'packages': packages})
