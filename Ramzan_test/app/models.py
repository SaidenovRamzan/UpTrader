# models.py
from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self", related_name="children", null=True, blank=True, on_delete=models.CASCADE
    )
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
