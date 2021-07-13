from django.db import models
from users.models import User
from survey_question_bindings.models import SurveyQuestionBinding

# Create your models here.


class SurveyResponse(models.Model):
    answer = models.TextField()
    submit_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    binding_id = models.ForeignKey(
        SurveyQuestionBinding, null=True, on_delete=models.DO_NOTHING
    )
