from django.contrib import admin
from .models import SurveyLog

# Register your models here.


class SurveyLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "timestamp",
        "type",
        "meta",
        "survey_id",
    )


admin.site.register(SurveyLog, SurveyLogAdmin)
