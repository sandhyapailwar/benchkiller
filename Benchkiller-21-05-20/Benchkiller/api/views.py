from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from crm.models.contact import Contact
from campaign.models.activity import Activity
from campaign.models.campaign import Campaign
from campaign.models.campaign_attachment import CampaignAttachment
from agent.serializers import ActivitySerializer
from agent.serializers import ContactSerializer
from agent.serializers import CampaignSerializer
from agent.serializers import CampaignAttachmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "is_staff")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Activities to be viewed.
    """

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=True, methods=["put"], name="change_state")
    def sent(self, request, pk=None):
        activity = self.get_object().mark_as_sent().save()
        return Response("OK")

    @action(detail=True, methods=["get"], name="get_attachments")
    def attachments(self, request, pk=None):
        attachment = self.get_object().campaign.campaign_attachments.get().attachment
        return HttpResponse(attachment, content_type="application/octet-stream")


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contacts to be viewed.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Campaigns to be viewed.
    """

    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignAttachmentViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows Campaign Attachments to be viewed.
    """

    queryset = CampaignAttachment.objects.all()
    serializer_class = CampaignAttachmentSerializer
