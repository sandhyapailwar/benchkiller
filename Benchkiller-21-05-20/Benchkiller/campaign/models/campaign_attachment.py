"""
This is the docstring for the campaign_attachment.py module
"""
from django.db import models


class CampaignAttachment(models.Model):
    """
    This is a class that defines Campaign Attachment model

    Attributes
    ----------
    state: models.TextField
    comment: models.TextField
    stateModified: datetime.datetime
    notifyAfter: datetime.datetime
    campaign: models.ForeignKey

    """

    attachment = models.FileField(null=True)
    campaign = models.ForeignKey(
        "campaign.Campaign",
        on_delete=models.CASCADE,
        related_name="campaign_attachments",
    )

    def __str__(self):
        return f"{self.campaign}"
