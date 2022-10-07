"""
This is the docstring for the campaign_attachment.py module
"""
from django.db import models


class CampaignPredicate(models.Model):
    """
    This is a class that defines Campaign Attachment model

    Attributes
    ----------
    name: str
    campaign: campaign.models.campaign.Campaign
    active: bool
    created: datetime
    modified: datetime

    """

    PREDICATE_CONTACT_STATE = "contact__state"
    PREDICATE_CONTACT_EMAIL = "contact__email"
    PREDICATE_CONTACT_FIRST_NAME = "contact__first_name"
    PREDICATE_CONTACT_LAST_NAME = "contact__last_name"
    PREDICATE_CONTACT_TYPE = "contact_role"

    PREDICATE_LOCATION_REGION = "role__location__region"
    PREDICATE_LOCATION_COUNTRY = "role__location__country"
    PREDICATE_LOCATION_LOCATION = "role__location__location"

    PREDICATE_ROLE_PRIMARY_SKILL = "role__primary_skill__name"
    PREDICATE_ROLE_SECONDARY_SKILLS = "role__secondary_skills"
    PREDICATE_ROLE = "role__name"
    PREDICATE_ROLE_REQUIREMENTS = "role__requirements"
    PREDICATE_ROLE_STATE = "role__state"
    PREDICATE_ROLE_FROM_LEVEL = "role__from_level__title"
    PREDICATE_ROLE_TO_LEVEL = "role__to_level__title"
    PREDICATE_ROLE_ID = "role__import_key"

    PREDICATE_OPPORTUNITY_NAME = "opportunity__opportunity_name"

    PREDICATES = (
        (PREDICATE_CONTACT_STATE, "Contact state"),
        (PREDICATE_CONTACT_TYPE, "Contact Type"),
        (PREDICATE_CONTACT_EMAIL, "Contact's Email"),
        (PREDICATE_CONTACT_FIRST_NAME, "Contact's First Name"),
        (PREDICATE_CONTACT_LAST_NAME, "Contact's Last Name"),
        (PREDICATE_ROLE, "Role Name"),
        (PREDICATE_ROLE_REQUIREMENTS, "Requirements"),
        (PREDICATE_ROLE_STATE, "Status"),
        (PREDICATE_ROLE_FROM_LEVEL, "From Level"),
        (PREDICATE_ROLE_TO_LEVEL, "To Level"),
        (PREDICATE_ROLE_ID, "Role ID"),
        (PREDICATE_ROLE_PRIMARY_SKILL, "Primary Skill"),
        (PREDICATE_ROLE_SECONDARY_SKILLS, "Secondary Skills"),
        (PREDICATE_LOCATION_REGION, "Region"),
        (PREDICATE_LOCATION_COUNTRY, "Country"),
        (PREDICATE_LOCATION_LOCATION, "Location"),
        (PREDICATE_OPPORTUNITY_NAME, "Opportunity"),
    )

    CONDITION_IS = "__exact"
    CONDITION_STARTS_WITH = "__istartswith"
    CONDITION_ENDS_WITH = "__iendswith"
    CONDITION_CONTAINS = "__icontains"

    CONDITIONS = (
        (CONDITION_CONTAINS, "Contains"),
        (CONDITION_IS, "Is"),
        (CONDITION_STARTS_WITH, "Starts with"),
        (CONDITION_ENDS_WITH, "Ends with"),
    )

    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(
        "campaign.Campaign",
        on_delete=models.CASCADE,
        related_name="campaign_predicates",
    )
    predicate_field = models.CharField(
        max_length=255, choices=PREDICATES, null=True, blank=False
    )
    predicate_condition = models.CharField(
        max_length=255,
        choices=CONDITIONS,
        null=False,
        blank=False,
        default=CONDITION_CONTAINS,
    )
    predicate_value = models.TextField(null=True)
    inverse = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Predicate> {self.name}"

    class Meta:
        verbose_name_plural = "Triggers"
        verbose_name = "Trigger"
