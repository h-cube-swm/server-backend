from django.http import HttpResponse, HttpRequest
from django.views import View
from survey_responses.models import SurveyResponse
from surveys.models import Survey
from utils import utils, responses

# Create your views here.


class ResponseView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        if not utils.is_valid_uuid(id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(result_link=id)
        if not survey.count():
            return utils.send_json(responses.invalidResultID)

        survey_responses = SurveyResponse.objects.filter(survey_id=survey[0]).values(
            "answer", "submit_time"
        )

        survey_all_fields = utils.to_dict(survey)[0]["fields"]

        survey_question = (
            {"title": survey_all_fields["title"]}
            | {"description": survey_all_fields["description"]}
            | survey_all_fields["contents"]
        )

        survey_responses = list(survey_responses)

        result = responses.ok.copy()
        result["result"] = {}
        result["result"]["survey"] = survey_question
        result["result"]["answers"] = survey_responses
        return utils.send_json(result)

    def post(self, request: HttpRequest, id: str) -> HttpResponse:
        if not utils.is_valid_uuid(id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)

        if not request.body:
            return utils.send_json(responses.illegalArgument)

        body_keys = ["answer"]
        request_dict = utils.json_to_dict(request.body)

        # request.body에서 딕셔너리 추출
        dic = utils.pop_args(request_dict, *body_keys)

        # 해당 answer 파라미터가 안 담겨서 요청 오면 에러 처리
        if None in list(dic.values()):
            return utils.send_json(responses.illegalArgument)

        survey = survey.first()
        SurveyResponse.objects.create(answer=dic["answer"], survey_id=survey)

        return utils.send_json(responses.createResponseSucceed)

    def put(self, request: HttpRequest, id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def delete(self, request: HttpRequest, id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)
