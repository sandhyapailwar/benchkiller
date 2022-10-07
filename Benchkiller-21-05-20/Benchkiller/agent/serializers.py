"""
Serializers for clas Contact and class Activity.
"""
from crm.models.contact import Contact
from campaign.models.activity import Activity
from campaign.models.campaign import Campaign
from campaign.models.campaign_attachment import CampaignAttachment

from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    """
     Serializer class for Contact model class.
     """

    class Meta:
        model = Contact
        fields = "__all__"


class CampaignAttachmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for Campaign Attachment model class.
    """

    class Meta:
        model = CampaignAttachment
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    """
     Serializer class for Campaign model class.
     """

    campaign_attachments = CampaignAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializer class for Activity model class.
    """

    bcc_contacts = ContactSerializer(many=True, read_only=True)
    other_contacts = ContactSerializer(many=True, read_only=True)
    contact = ContactSerializer(many=True, read_only=True)
    campaign = CampaignSerializer(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = "__all__"
