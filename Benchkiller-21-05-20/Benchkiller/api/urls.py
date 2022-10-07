from django.conf.urls import url, include
from rest_framework import routers

from api.views import ContactViewSet
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"contacts", ContactViewSet)

urlpatterns = [url(r"^", include(router.urls))]
