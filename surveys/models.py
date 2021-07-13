from django.db import models
from users.models import User

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

TYPE_SCROLL = "scroll"
TYPE_SLIDE = "slide"

TYPE_CHOICES = ((TYPE_SCROLL, "Scroll"), (TYPE_SLIDE, "Slide"))


class Survey(models.Model):
    title = models.TextField()
    description = models.TextField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    meta = models.JSONField(null=True)
    view_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    user_id = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
