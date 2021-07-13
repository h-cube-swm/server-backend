from django.db import models
from surveys.models import Survey

# Create your models here.


class SurveyLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.TextField()
    meta = models.TextField(null=True)
    survey_id = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "survey_logs"