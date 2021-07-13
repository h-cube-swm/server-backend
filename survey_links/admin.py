from django.contrib import admin
from .models import SurveyLink

# Register your models here.


class SurveyLinkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "hash",
        "survey_id",
    )


admin.site.register(SurveyLink, SurveyLinkAdmin)
