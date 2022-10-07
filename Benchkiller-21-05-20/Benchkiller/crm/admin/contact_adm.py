"""
Representation of admin for model Contact
"""
from django.contrib import admin
from crm.models.contact import Contact


class ContactAdm(admin.ModelAdmin):
    """Creates admin for class Contact"""

    fields = ["state", "first_name", "last_name", "email", "display_name"]
    search_fields = ("display_name", )
    list_filter = ("state", )
    list_display = ["display_name"]




admin.site.register(Contact, ContactAdm)
