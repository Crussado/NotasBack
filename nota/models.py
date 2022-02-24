from django.db import models


class Nota(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)

    def __str__(self):
        return self.title
