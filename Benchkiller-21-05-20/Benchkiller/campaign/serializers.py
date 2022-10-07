"""
Serializers for clas Contact and class Activity.
"""
from django.contrib.auth.models import User

from campaign.models.activity import Activity
from campaign.models.campaign_attachment import CampaignAttachment

from rest_framework import serializers

from crm.models.contact import Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "is_staff")


class CampaignAttachmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for Campaign Attachment model class.
    """

    class Meta:
        model = CampaignAttachment
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "first_name", "last_name", "full_name", "email"


class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializer class for Activity model class.
    """

    bcc_contacts = ContactSerializer(many=True, read_only=True)
    contact = ContactSerializer(read_only=True)
    other_contacts = ContactSerializer(many=True, read_only=True)
    attachments = CampaignAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = (
            "id",
            "contact",
            "other_contacts",
            "bcc_contacts",
            "subject",
            "body",
            "html_body",
            "attachments",
        )
