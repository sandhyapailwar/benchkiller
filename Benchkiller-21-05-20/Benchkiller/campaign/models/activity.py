"""
This is the docstring for the activity.py module
"""
from django.db import models
from django.utils import timezone


class Activity(models.Model):
    """
    This is a class that defines Activity model

    Attributes
    ----------
    state: models.CharField
    comment: models.TextField
    state_modified: datetime.datetime
    notify_after: datetime.datetime
    campaign: models.ForeignKey
    opportunity: models.ForeignKey
    contact: models.ForeignKey
    contacts: models.ManyToMany
    """

    ACTIVITY_NEW = "new"
    ACTIVITY_AWAITING = "awaiting"
    ACTIVITY_IN_PROGRESS = "progress"
    ACTIVITY_DONE = "done"
    ACTIVITY_FAILED = "failed"
    STATES = (
        (ACTIVITY_NEW, "New"),
        (ACTIVITY_AWAITING, "Awaiting"),
        (ACTIVITY_IN_PROGRESS, "In Progress"),
        (ACTIVITY_DONE, "Done"),
        (ACTIVITY_FAILED, "Failed"),
    )

    state = models.CharField(
        max_length=20, null=False, choices=STATES, default=ACTIVITY_NEW
    )
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    notify_after = models.DateTimeField(null=True)

    campaign = models.ForeignKey(
        "campaign.Campaign",
        on_delete=models.CASCADE,
        related_name="campaign_activity",
        null=True,
    )
    wave = models.ForeignKey(
        "campaign.Wave",
        on_delete=models.CASCADE,
        related_name="wave_activities",
        null=True,
    )

    contact = models.ForeignKey(
        "crm.Contact",
        on_delete=models.CASCADE,
        related_name="contact_activities",
        blank=True,
    )

    other_contacts = models.ManyToManyField(
        "crm.Contact", related_name="other_contact_activities", blank=True
    )
 
    bcc_contacts = models.ManyToManyField(
        "crm.Contact", related_name="bcc_contacts_activities", blank=True
    )

    subject = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    html_body = models.TextField(null=True, blank=True)

    def mark_as_sent(self):
        self.state = self.ACTIVITY_DONE
        self.log_line("Activity marked as completed")
        return self

    def mark_as_in_progress(self):
        self.state = self.ACTIVITY_IN_PROGRESS
        return self

    def __str__(self):
        return f"{self.state}"

    @property
    def attachments(self):
        return self.campaign.campaign_attachments.all()

    def log(self, message):
        if not self.comment:
            self.comment = ""
        self.comment += f"""[{ timezone.now():%Y-%m-%d %H:%M:%S }] { message }"""
        return self

    def log_line(self, message):
        return self.log(message + "\n")

    class Meta:
        verbose_name_plural = "Activities"
