from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
