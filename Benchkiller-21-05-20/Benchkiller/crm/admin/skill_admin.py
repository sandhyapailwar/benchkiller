"""
Representation of a model's Skill in the admin interface
"""

from django.contrib import admin

from crm.models.skill import Skill


class SkillAdmin(admin.ModelAdmin):
    """
    Admin class related to Skill class of Model

    """

    fields = ["name", "role_skills"]


admin.site.register(Skill, SkillAdmin)
