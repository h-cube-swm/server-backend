from django.contrib import admin
from .models import Survey

# Register your models here.


class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "status",
        "contents",
        "survey_link",
        "response_link",
        "created_datetime",
        "updated_datetime",
        "user_email",
    )


admin.site.register(Survey, SurveyAdmin)
