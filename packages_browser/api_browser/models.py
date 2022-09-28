from django.db import models


class Packages(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    guid = models.URLField(max_length=100)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    pubDate = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"
