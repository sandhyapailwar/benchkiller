"""
CRM Models class Opportunity
"""
from django.db import models


class Opportunity(models.Model):
    """
    Adds class Opportunity which represents opportunity in model

    Attributes
    ----------
    opportunity_name: str
    role: models.ForeignKey

    """

    opportunity_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.opportunity_name}"

    class Meta:
        verbose_name_plural = "Opportunities"
