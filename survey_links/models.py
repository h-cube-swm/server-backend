from django.db import models
from surveys.models import Survey

# Create your models here.


class SurveyLink(models.Model):
    hash = models.TextField()
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        db_table = "survey_links"
