from django.db import models
import uuid

# Create your models here.


STATUS_EDITING = "editing"
STATUS_PUBLISHED = "published"
STATUS_CLOSED = "closed"
STATUS_DELETED = "deleted"

STATUS_CHOICES = (
    (STATUS_EDITING, "Editing"),
    (STATUS_PUBLISHED, "Published"),
    (STATUS_CLOSED, "Closed"),
    (STATUS_DELETED, "Deleted"),
)


class Survey(models.Model):
    title = models.TextField(default="", blank=True)
    description = models.TextField(null=True, default="", blank=True)
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=20, default=STATUS_EDITING
    )
    contents = models.JSONField(default=dict, blank=True)
    survey_link = models.UUIDField(default=uuid.uuid4, editable=False)
    result_link = models.UUIDField(default=uuid.uuid4, editable=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    user_email = models.EmailField(max_length=320, null=True, blank=True)

    class Meta:
        db_table = "surveys"

    def __str__(self):
        return str(self.id)
