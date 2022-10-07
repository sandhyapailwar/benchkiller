"""
Representation of admin for model OpportunityContact
"""
from django.contrib import admin
from crm.models.opportunitycontact import OpportunityContact


class OpportunityContactAdm(admin.ModelAdmin):
    """Creates admin for class OpportunityContact"""

    fields = ["contact", "opportunity", "role", "contact_role"]
    list_display = "contact_full_name", "contact_role", "opportunity_name", "role"
    list_filter = ["contact_role"]

    def contact_full_name(self, obj):
        return obj.contact.full_name

    contact_full_name.short_description = "Contact"

    def opportunity_name(self, obj):
        return obj.opportunity.opportunity_name

    opportunity_name.short_description = "Opportunity"


admin.site.register(OpportunityContact, OpportunityContactAdm)
