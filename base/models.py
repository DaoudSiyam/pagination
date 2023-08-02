from django.db import models


class Video(models.Model):
    title = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    is_watched = models.BooleanField(default = False)

    def __str__(self):
        return self.title