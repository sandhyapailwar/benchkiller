"""
This is the docstring for the campaign_post_action.py module
"""
from django.db import models


class CampaignPostAction(models.Model):
    """
    This is a class that defines Campaign Post Action model

    Attributes
    ----------
    name: str
    campaign: campaign.models.campaign.Campaign
    active: bool
    created: datetime
    modified: datetime

    """

    FIELD_CONTACT_STATE = "contact__state"

    FIELDS = ((FIELD_CONTACT_STATE, "Contact state"),)

    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(
        "campaign.Campaign",
        on_delete=models.CASCADE,
        related_name="campaign_post_actions",
    )
    field = models.CharField(max_length=255, choices=FIELDS, null=True, blank=False)
    value = models.TextField(null=True)

    def __str__(self):
        return f"<Post Action> {self.name}"
