from django.contrib import admin
from .models import SurveyQuestion

# Register your models here.


class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "hash")


admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
