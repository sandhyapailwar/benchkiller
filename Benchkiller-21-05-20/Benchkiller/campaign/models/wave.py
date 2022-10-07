from django.db import models


class Wave(models.Model):
    campaign = models.ForeignKey(
        "campaign.Campaign", on_delete=models.CASCADE, related_name="campaign_waves"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.pk}"
