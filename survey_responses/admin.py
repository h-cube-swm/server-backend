from django.contrib import admin
from .models import SurveyResponse

# Register your models here.


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "answer", "submit_time", "survey_id")


admin.site.register(SurveyResponse, SurveyResponseAdmin)
