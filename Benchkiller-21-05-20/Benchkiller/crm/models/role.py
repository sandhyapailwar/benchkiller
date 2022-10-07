"""
CRM Models class Role
"""
from django.db import models


class Role(models.Model):
    """
    Model class Level serves to store data of the role such as requirements, state, location, dates

    Attributes
    ----------
    name: str
    requirements: str
    state: str
    location: models.ForeignKey
    valid_from: datetime.datetime
    valid_till: datetime.datetime

    """

    name = models.CharField(max_length=200)
    requirements = models.TextField()
    state = models.CharField(max_length=200)
    location = models.ForeignKey("crm.Location", on_delete=models.CASCADE)
    valid_from = models.DateTimeField("date valid from", null=True)
    valid_till = models.DateTimeField("date valid till", null=True)
    opportunity = models.ForeignKey(
        "crm.Opportunity",
        on_delete=models.CASCADE,
        related_name="opportunity_roles",
        null=True,
    )

    from_level = models.ForeignKey(
        "crm.Level",
        related_name="roles_from_level",
        null=True,
        on_delete=models.CASCADE,
    )
    to_level = models.ForeignKey(
        "crm.Level", related_name="roles_to_level", null=True, on_delete=models.CASCADE
    )
    primary_skill = models.ForeignKey(
        "crm.Skill", related_name="skill_roles", default=None, on_delete=models.CASCADE
    )
    secondary_skills = models.TextField(default=None, blank=True, null=True)
    import_key = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.name}"
