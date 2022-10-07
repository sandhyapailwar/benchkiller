from django.conf.urls import url, include
from rest_framework import routers

from campaign.views import ActivityViewSet

# from campaign.views import CampaignViewSet
# from campaign.views import CampaignAttachmentViewSet


router = routers.DefaultRouter()
router.register(r"activity", ActivityViewSet)
# router.register(r"campaign/attachments", CampaignAttachmentViewSet)
# router.register(r"campaign", CampaignViewSet)

urlpatterns = [url(r"^", include(router.urls))]
