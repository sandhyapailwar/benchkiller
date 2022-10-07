"""
CRM Models class Skill
"""
from django.db import models


class Skill(models.Model):
    """
    Model class Skill serves to store data of the role's name and contains cross-reference to the model Role

    Attributes
    ----------
    name: str

    """

    name = models.TextField()

    def __str__(self):
        return f"{self.name}"
