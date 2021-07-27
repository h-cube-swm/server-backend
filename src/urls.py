"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from surveys.views import LinkView
from surveys.views import SurveyView
from surveys.views import SurveyEndView
from survey_responses.views import ResponseView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin", admin.site.urls),
    path("", include("views.urls")),
    path("link", LinkView.as_view()),
    path("surveys/<str:survey_id>", SurveyView.as_view()),
    path("surveys/<str:survey_id>/end", SurveyEndView.as_view()),
    path(
        "surveys/<str:id>/responses", ResponseView.as_view()
    ),  # <str:id> -> id가 survey_id이거나 result_id이거나 할 수 있음
]
urlpatterns += staticfiles_urlpatterns()
