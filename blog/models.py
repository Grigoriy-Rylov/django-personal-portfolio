from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField()
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
