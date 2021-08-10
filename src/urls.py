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
from surveys.views import SurveyEmailView
from survey_responses.views import ResponseView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("views.urls")),
    path("link", LinkView.as_view()),
    path("surveys/<str:survey_id>", SurveyView.as_view()),
    # surveys/<str:survey_id> 는 그 id가
    # survey_link일 경우 (설문을 수정중일 때)
    # response_link일 경우 (설문에 응답하기 위해 설문지를 조회할 때)
    # 일 수도 있음.
    path("surveys/<str:survey_id>/end", SurveyEndView.as_view()),
    path(
        "surveys/<str:id>/responses", ResponseView.as_view()
    ),
    # surveys/<str:id>/responses 엔드포인트의 경우
    # <str:id> -> id가
    # survey_link이거나             (응답 리스트를 조회할 경우)
    # response_link이거나 할 수 있음  (실제 응답이 들어올 때)
    path("surveys/<str:survey_id>/emails", SurveyEmailView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
