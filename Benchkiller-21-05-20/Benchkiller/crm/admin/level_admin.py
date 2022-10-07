"""
Representation of a model's Level in the admin interface

"""

from django.contrib import admin

from crm.models.level import Level


class LevelAdmin(admin.ModelAdmin):
    """
    Admin class related to Level class of Model

    """

    list_display = "title", "number"
    fields = ["title", "number"]


admin.site.register(Level, LevelAdmin)
