from django.db import models
from surveys.models import Survey
from survey_questions.models import SurveyQuestion

# Create your models here.


class SurveyQuestionBinding(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    question_id = models.ForeignKey(SurveyQuestion, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "survey_question_bindings"
