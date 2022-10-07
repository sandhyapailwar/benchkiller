"""
CRM Models class Level
"""
from django.db import models


class Level(models.Model):
    """
    Model class Level serves to store data of the role's Level such as title and number

    Attributes
    ----------
    title: str
    number: int

    """

    title = models.CharField(max_length=200)
    number = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title} {self.number}"
