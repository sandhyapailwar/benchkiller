"""
Representation of a model's Role in the admin interface
"""

from django.contrib import admin

from crm.models.opportunitycontact import OpportunityContact
from crm.models.role import Role


class OpportunityContactAdminInline(admin.StackedInline):
    """Creates admin for class OpportunityContact"""

    model = OpportunityContact
    fields = [("opportunity", "contact")]
    readonly_fields = "opportunity", "contact"
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


class RoleAdmin(admin.ModelAdmin):
    """
    Admin class related to Role class of Model

    """

    fields = (
        "opportunity",
        "name",
        "requirements",
        "state",
        "primary_skill",
        "secondary_skills",
        "location",
        "valid_from",
        "valid_till",
    )
    readonly_fields = (
        "opportunity",
        "name",
        "requirements",
        "state",
        "primary_skill",
        "secondary_skills",
        "location",
        "valid_from",
        "valid_till",
    )

    list_display = "name", "opportunity", "state", "valid_from", "valid_till"
    inlines = [OpportunityContactAdminInline]
    list_filter = ["state", "location__region", "location__country", "primary_skill"]

    filter_horizontal = [
        # "location__region",
        # "location__country",
    ]

    search_fields = ["opportunity__opportunity_name"]


admin.site.register(Role, RoleAdmin)
