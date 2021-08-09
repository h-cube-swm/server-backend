from django.contrib import admin
from .models import SurveyResponse

# Register your models here.


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "answer", "submit_time", "updated_datetime", "survey_id")


admin.site.register(SurveyResponse, SurveyResponseAdmin)
