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
    title = models.TextField(default="")
    description = models.TextField(null=True, default="")
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=20, default=STATUS_EDITING
    )
    contents = models.JSONField(default=dict)
    survey_link = models.UUIDField(default=uuid.uuid4, editable=False)
    result_link = models.UUIDField(default=uuid.uuid4, editable=False)
    view = models.TextField(default="설문 view타입을 넣어주세요")

    class Meta:
        db_table = "surveys"

    def __str__(self):
        return str(self.id)
