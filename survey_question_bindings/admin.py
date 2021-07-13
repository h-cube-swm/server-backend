from django.contrib import admin
from .models import SurveyQuestionBinding

# Register your models here.


class SurveyQuestionBindingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "survey_id",
        "question_id",
    )


admin.site.register(SurveyQuestionBinding, SurveyQuestionBindingAdmin)
