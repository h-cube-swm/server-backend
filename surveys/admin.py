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
        "link",
        "view",
    )


admin.site.register(Survey, SurveyAdmin)
