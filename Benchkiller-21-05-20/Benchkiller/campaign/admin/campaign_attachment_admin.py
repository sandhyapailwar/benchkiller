"""
Admin section for Campaign Attachemnt model
"""
from django.contrib import admin
from campaign.models.campaign_attachment import CampaignAttachment


class CampaignAttachmentAdmin(admin.ModelAdmin):
    """
    Class for Campaign Attachment admin
    """

    pass


admin.site.register(CampaignAttachment, CampaignAttachmentAdmin)
