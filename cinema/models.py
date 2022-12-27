from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.title)
