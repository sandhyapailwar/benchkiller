"""
This is the docstring for the campaign.py module
"""
from django.db import models


class Campaign(models.Model):
    """
    This is a class that defines Campaign model

    Attributes
    ----------
    start: datetime.datetime
    end: datetime.datetime
    created: datetime.datetime
    name: str
    template: str
    cc: crm.models.contact.Contact
    bcc: crm.models.contact.Contact
    """

    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    aggregate_activities = models.BooleanField("Do not create duplicates", default=True)
    subject = models.CharField(max_length=255, null=True, blank=False)
    template = models.TextField(null=False)
    html_template = models.TextField(null=True)
    cc = models.ManyToManyField(
        "crm.Contact", related_name="campaign_cc_contacts", blank=True
    )
    bcc = models.ManyToManyField(
        "crm.Contact", related_name="campaign_bcc_contacts", blank=True
    )


    def __str__(self):
        return f"{self.name}"
