"""
Admin section for Campaign model
"""
from django.contrib import admin

from campaign.models.campaign import Campaign
from campaign.models.campaign_attachment import CampaignAttachment
from campaign.models.campaign_predicate import CampaignPredicate
from campaign.models.campaign_property import CampaignProperty
from campaign.models.campaing_post_action import CampaignPostAction
from campaign.services.wave_wizard import wave_wizard


class CampaignAttachmentInLine(admin.StackedInline):
    """
     Class for CampaignAttachemnt in line
    """

    extra = 0
    model = CampaignAttachment


class CampaignPredicateInLine(admin.StackedInline):
    """
     Class for CampaignPredicate in line
    """

    extra = 0
    fields = (
        ("name", "active"),
        ("predicate_field", "predicate_condition", "inverse"),
        "predicate_value",
    )
    model = CampaignPredicate


class CampaignPropertyInLine(admin.StackedInline):
    """
     Class for CampaignProperty in line
    """

    extra = 0
    fields = "name", "value"  # , "comment"
    model = CampaignProperty


class CampaignPostActionInLine(admin.StackedInline):
    """
     Class for CampaignPostAction in line
    """

    extra = 0
    fields = "name", "field", "value"  # , "comment"
    model = CampaignPostAction


class CampaignAdmin(admin.ModelAdmin):
    """
    Class for Campaign admin
    """

    list_display = "name", "start", "end", "created"
    save_as = True
    fields = (
        ("name", "aggregate_activities"),
        # ("start", "end"),
        ("cc", "bcc"),
        "subject",
        ("template", "html_template"),
    )
    actions = ["make_wave"]
    inlines = [
        CampaignAttachmentInLine,
        CampaignPropertyInLine,
        CampaignPredicateInLine,
        CampaignPostActionInLine,
    ]

    def make_wave(self, request, campaigns):
        for campaign in campaigns:
            wave_wizard(request, campaign)

    make_wave.short_description = "Start New Wave"


admin.site.register(Campaign, CampaignAdmin)
