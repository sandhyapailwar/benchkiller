"""
CRM Models class Contact
"""
from django.db import models


class Contact(models.Model):
    """
    Adds class Contact which represents contacts in model

    Attributes
    ----------
    state: str
    first_name: str
    last_name: str
    email: str

    """

    STATE_NEW = "new"
    STATE_ACTIVE = "active"
    STATE_INACTIVE = "inactive"

    VALID_STATES = {STATE_NEW, STATE_ACTIVE, STATE_INACTIVE}

    STATES = (
        (STATE_NEW, STATE_NEW),
        (STATE_ACTIVE, STATE_ACTIVE),
        (STATE_INACTIVE, STATE_INACTIVE),
    )

    state = models.CharField(max_length=30, choices=STATES, default=STATE_NEW)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True)
    display_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.full_name

    def mark_as_active(self):
        self.state = self.STATE_ACTIVE
        return self

    def set_state(self, value: str):
        if value in self.VALID_STATES:
            self.state = value
        return self

    @property
    def full_name(self):
#        return f"{self.first_name} {self.last_name}"
        return f"{self.display_name}"
