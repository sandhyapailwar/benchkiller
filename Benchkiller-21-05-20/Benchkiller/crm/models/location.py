"""
CRM Models class Location
"""
from django.db import models


class Location(models.Model):
    """
    Model class Location serves to store data of the role's location such as title, location, country, region

    Attributes
    ----------
    location: str
    country: str
    region: str

    """

    location = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.region} {self.country} {self.location}"
