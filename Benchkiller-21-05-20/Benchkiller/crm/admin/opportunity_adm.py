"""
Representation of admin for model Opportunity
"""
from django.contrib import admin
from crm.models.opportunity import Opportunity
from crm.models.opportunitycontact import OpportunityContact


class OpportunityContactAdminInline(admin.StackedInline):
    """Creates admin for class OpportunityContact"""

    model = OpportunityContact
    fields = ["role", "contact"]
    list_display = "role", "contact_first_name", "contact_last_name", "opportunity_name"

    def contact_first_name(self, obj):
        return obj.contact.first_name

    contact_first_name.short_description = "First name"

    def contact_last_name(self, obj):
        return obj.contact.last_name

    contact_last_name.short_description = "Last name"

    def opportunity_name(self, obj):
        return obj.opportunity.opportunity_name

    opportunity_name.short_description = "Opportunity"


class OpportunityAdm(admin.ModelAdmin):
    """Creates admin for class Opportunity"""

    fields = ["opportunity_name"]
    inlines = [OpportunityContactAdminInline]


admin.site.register(Opportunity, OpportunityAdm)
