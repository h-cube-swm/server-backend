from django.db import models

# Create your models here.


class SurveyQuestion(models.Model):
    question = models.JSONField()
    hash = models.TextField()
