import os
from datetime import datetime
from django.db import models


def task_path(instance: any, filename: str) -> str:
    now = datetime.utcnow()
    return os.path.join(
        f"tasks_{ instance.user.id }",
        now.strftime("%Y-%m-%d"),
        now.strftime("%H.%M"),
        filename,
    )


class EtlTask(models.Model):
    TASK_NEW = "new"
    TASK_IN_PROGRESS = "progress"
    TASK_COMPLETED = "done"
    TASK_FAILED = "failed"

    STATES = (
        (TASK_NEW, TASK_NEW),
        (TASK_IN_PROGRESS, TASK_IN_PROGRESS),
        (TASK_COMPLETED, TASK_COMPLETED),
        (TASK_FAILED, TASK_FAILED),
    )

    file = models.FileField(upload_to=task_path)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, editable=False)
    state = models.CharField(
        max_length=16, choices=STATES, default=TASK_NEW, editable=False
    )
    log = models.TextField(null=True, editable=False)
