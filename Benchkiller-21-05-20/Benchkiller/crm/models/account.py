"""
CRM Models class Account
"""
from django.db import models


class Account(models.Model):
    """
    Adds class Account which represents accounts in model

    Attributes
    ----------
    account_name: str
    contacts: models.ManyToManyField
    opportunities: models.ManyToManyField

    """

    account_name = models.CharField(max_length=20)
    contacts = models.ManyToManyField(
        "crm.Contact", related_name="contact_accounts", blank=True
    )
    opportunities = models.ManyToManyField(
        "crm.Opportunity", related_name="opportunity_accounts", blank=True
    )

    def __str__(self):
        return f"{self.account_name}"
