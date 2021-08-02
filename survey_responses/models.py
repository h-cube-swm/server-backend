from django.db import models
from django.db.models.deletion import DO_NOTHING
from surveys.models import Survey

# Create your models here.


class SurveyResponse(models.Model):
    answer = models.JSONField()
    submit_time = models.DateTimeField(auto_now_add=True)
    survey_id = models.ForeignKey(Survey, on_delete=DO_NOTHING)

    class Meta:
        db_table = "survey_responses"
