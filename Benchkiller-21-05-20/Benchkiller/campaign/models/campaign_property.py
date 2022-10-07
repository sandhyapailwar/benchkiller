"""
This is the docstring for the campaign_property.py module
"""
from django.db import models


class CampaignProperty(models.Model):
    """
    This is a class that defines Campaign Attachment model

    Attributes
    ----------
    name: models.CharField
    value: models.TextField
    comment: datetime.TextField
    campaign: models.ForeignKey

    """

    name = models.CharField(max_length=255)
    value = models.TextField(null=True)
    comment = models.TextField(null=True)
    campaign = models.ForeignKey(
        "campaign.Campaign",
        on_delete=models.CASCADE,
        related_name="campaign_properties",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Template properties"
        verbose_name = "Template property"
