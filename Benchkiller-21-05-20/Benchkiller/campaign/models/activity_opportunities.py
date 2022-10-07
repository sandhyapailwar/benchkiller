"""
This is the docstring for the activity.py module
"""
from django.db import models
from django.utils import timezone


class ActivityOpportunityContact(models.Model):
    """
    This is a class that defines Activity model

    Attributes
    ----------
    activity: models.ForeignKey
    opportunty_contact: models.ForeignKey
    """

    activity = models.ForeignKey(
        "campaign.Activity",
        on_delete=models.CASCADE,
        related_name="activity_opportunity_contacts",
        null=True,
    )
    opportunity_contact = models.ForeignKey(
        "crm.OpportunityContact",
        on_delete=models.CASCADE,
        related_name="opportunity_contact_activities",
        null=True,
    )
    opportunity = models.ForeignKey(
        "crm.Opportunity",
        on_delete=models.CASCADE,
        related_name="opportunity_activity_contacts",
        default=None,
    )
    role = models.ForeignKey(
        "crm.Role",
        on_delete=models.CASCADE,
        related_name="role_activity_contacts",
        default=None,
    )

    contact_role = models.CharField(max_length=20, null=True)
