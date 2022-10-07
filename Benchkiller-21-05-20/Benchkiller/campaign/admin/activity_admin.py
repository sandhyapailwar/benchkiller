"""
Admin section for Opportunity Campaign model
"""
from django.contrib import admin
from django import forms

from campaign.models.activity import Activity
from campaign.models.activity_opportunities import ActivityOpportunityContact
from crm.models.opportunitycontact import OpportunityContact


class ActivityForm(forms.ModelForm):
    answer = forms.CharField()

    class Meta:
        model = Activity
        fields = "__all__"


class CampaignOpportunityContactsInLine(admin.StackedInline):
    """
     Class for CampaignPredicate in line
    """

    extra = 0
    fields = (("opportunity_contact", "contact_role"), ("opportunity", "role"))
    readonly_fields = "opportunity_contact", "opportunity", "role", "contact_role"
    model = ActivityOpportunityContact


class ActivityAdmin(admin.ModelAdmin):
    """
    Class for Opportunity Campaign admin
    """

    list_display = "get_campaign", "wave", "get_contact", "state"
    fields = (
        ("campaign", "state"),
        # ("opportunity", "role"),
        "contact",
        ("other_contacts", "bcc_contacts"),
        "subject",
        ("body", "html_body"),
        "comment",
    )
    readonly_fields = ("state", "comment")
    list_filter = ["state"]
    inlines = [CampaignOpportunityContactsInLine]

    def get_campaign(self, obj):
        return obj.campaign.name

    get_campaign.short_description = "Campaign"

    def get_contact(self, obj):
        return f"{obj.contact.full_name} <{obj.contact.email}>"

    get_contact.short_description = "Contact"

    def get_other_contacts(self, obj):
        return f"{obj.other_contacts.full_name} <{obj.other_contacts.email}>"

    get_other_contacts.short_description = "Other_Contacts"

    def get_opportunity(self, obj):
        return obj.opportunity.opportunity_name

    get_opportunity.short_description = "Opportunity"


admin.site.register(Activity, ActivityAdmin)
