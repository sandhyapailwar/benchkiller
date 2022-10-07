"""
Representation of a model's Location in the admin interface
"""


from django.contrib import admin

from crm.models.location import Location


class LocationAdmin(admin.ModelAdmin):
    """
    Admin class related to Role class of Model

    """

    fields = ["location", "country", "region"]


admin.site.register(Location, LocationAdmin)
