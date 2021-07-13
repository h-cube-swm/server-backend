from django.contrib import admin
from .models import SurveyResponseLog

# Register your models here.


class SurveyResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "timestamp",
        "type",
        "meta",
        "user_id",
        "survey_id",
    )


admin.site.register(SurveyResponseLog, SurveyResponseLogAdmin)
