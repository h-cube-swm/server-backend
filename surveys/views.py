from django.http import HttpResponse, HttpRequest
from django.views import View
from surveys.models import Survey
from users.models import User
from survey_links.models import SurveyLink
from survey_questions.models import SurveyQuestion
from survey_question_bindings.models import SurveyQuestionBinding
from utils import utils, responses
import uuid

# Create your views here.


class LinkView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        survey = Survey.objects.create()
        result = responses.ok
        result["link"] = str(survey.survey_link)
        return utils.send_json(result)
        

class SurveyView(View):
    def get(self, request: HttpRequest, survey_id: uuid) -> HttpResponse:
        survey = Survey.objects.filter(survey_link=survey_id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)
        survey = utils.to_dict(survey)
        result = responses.ok
        result["result"] = survey
        return utils.send_json(result)

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass
