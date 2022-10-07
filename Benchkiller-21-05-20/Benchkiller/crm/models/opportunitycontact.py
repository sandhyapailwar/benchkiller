"""
CRM Models class OpportunityContact
"""
from django.db import models


class OpportunityContact(models.Model):
    """
    Adds class OpportunityContact which represents connection between opportunities and contacts

    Attributes
    ----------
    role: str
    contact: crm.models.contact.Contact
    opportunity: crm.models.opportunity.Opportunity
    """

    ROLE_PRIMARY = "primary"
    ROLE_KEYCONTACT = "key_contact"

    ROLES = ((ROLE_PRIMARY, "Primary Contact"), (ROLE_KEYCONTACT, "Key contact"))

    contact_role = models.CharField(max_length=20, choices=ROLES, default=ROLE_PRIMARY)
    contact = models.ForeignKey(
        "crm.Contact",
        on_delete=models.CASCADE,
        related_name="contacts_opportunity",
        default=None,
    )
    opportunity = models.ForeignKey(
        "crm.Opportunity",
        on_delete=models.CASCADE,
        related_name="opportunity_contacts",
        default=None,
    )
    role = models.ForeignKey(
        "crm.Role", on_delete=models.CASCADE, related_name="role_contacts", default=None
    )

    def __str__(self):
        return f"{self.contact.full_name}"
