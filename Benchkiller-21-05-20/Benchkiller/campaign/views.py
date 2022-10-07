from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from crm.models.contact import Contact
from campaign.models.activity import Activity
from campaign.services.complete_wizard import complete_activity_wizard
from campaign.models.campaign_attachment import CampaignAttachment
from campaign.serializers import (
    ActivitySerializer,
    CampaignAttachmentSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Activities to be viewed.
    """

    filter_backends = (DjangoFilterBackend,)
    filter_fields = "state", "contact__state"
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=True, methods=["get"], serializer_class=ActivitySerializer)
    def sent(self, request, pk=None):
        activity = self.get_object()
        complete_activity_wizard(activity)
        activity.mark_as_sent().save()
        return Response(activity)

    @action(detail=True, methods=["get"], serializer_class=ActivitySerializer)
    def in_progress(self, request, pk=None):
        activity = self.get_object().mark_as_in_progress()
        activity.save()
        # activity.contact.mark_as_active().save()
        return Response(dict(status="In Progress"))
