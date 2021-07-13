from django.db import models
from users.models import User
from surveys.models import Survey

# Create your models here.


class SurveyResponseLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.TextField()
    meta = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    survey_id = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "survey_response_logs"
