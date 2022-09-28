import lxml.etree
import urllib.request
from api_browser.models import Packages


def fetch_packages_data():
    response = urllib.request.urlopen('https://pypi.org/rss/packages.xml')
    tree = lxml.etree.parse(response)
    items = tree.xpath("//item")

    for item in items:
        if item.find("author") == None:
            find_author = 'unknown author'
        else:
            find_author = item.find("author").text
        Packages.objects.get_or_create(
            title=item.find("title").text,
            defaults={
                "title": item.find("title").text,
                "link": item.find("link").text,
                "guid": item.find("guid").text,
                "description": item.find("description").text,
                "author": find_author,
                "pubDate": item.find("pubDate").text})

    print('Packages data were updated')
