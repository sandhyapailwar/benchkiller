import os

from django.contrib import admin
from django.conf import settings

from .models import EtlTask
from .services.etl import etl_task


class EtlTaskAdmin(admin.ModelAdmin):
    """
    Class for EtlTask admin
    """

    model = EtlTask

    empty_value_display = "-empty-"
    readonly_fields = "user", "log"

    def save_model(self, request, obj: EtlTask, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        etl_task(os.path.join(settings.MEDIA_ROOT, obj.file.name))


admin.site.register(EtlTask, EtlTaskAdmin)
