"""
Representation of admin for model Account
"""
from django.contrib import admin
from crm.models.account import Account


class AccountAdm(admin.ModelAdmin):
    """Creates admin for class Account"""

    fields = ["account_name", "contacts", "opportunities"]


admin.site.register(Account, AccountAdm)
