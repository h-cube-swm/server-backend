from django.http import HttpResponse, HttpRequest
from django.views import View
from surveys.models import Survey
from users.models import User
from survey_links.models import SurveyLink
from survey_questions.models import SurveyQuestion
from survey_question_bindings.models import SurveyQuestionBinding
from utils import utils, responses

# Create your views here.


class RootView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        result = responses.ok
        

    def post(self, request: HttpRequest) -> HttpResponse:
        pass


class ElementView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass
