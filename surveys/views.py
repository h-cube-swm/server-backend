from django.http import HttpResponse, HttpRequest
from django.views import View
from surveys.models import Survey
from utils import utils, responses
import datetime

# Create your views here.


# /link
class LinkView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        survey = Survey.objects.create()
        result = responses.ok
        result["result"] = str(survey.survey_link)
        return utils.send_json(result)

    def post(self, request: HttpRequest) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def put(self, request: HttpRequest) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def delete(self, request: HttpRequest) -> HttpResponse:
        return utils.send_json(responses.noAPI)


# /surveys/{survey_id}
class SurveyView(View):
    def get(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=survey_id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)
        survey = utils.to_dict(survey)[0]["fields"]
        result = responses.ok
        result["result"] = survey
        return utils.send_json(result)

    def post(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def put(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=survey_id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)
        if survey[0].status != "editing":
            return utils.send_json(responses.surveyCannotEdit)

        body_keys = ["title", "description", "contents"]
        request_dict = utils.json_to_dict(request.body)

        # request.body에서 딕셔너리 추출
        dic = utils.pop_args(request_dict, *body_keys)

        # 위 파라미터 중 1개라도 담겨서 오지 않는 경우
        if [None] * len(body_keys) == list(dic.values()):
            return utils.send_json(responses.illegalArgument)

        original_survey = survey
        survey = utils.to_dict(survey)[0]

        # 데이터베이스 update가 문제 없게 동작하기 위한 분기 처리
        if dic["title"] is None:
            dic["title"] = survey["fields"]["title"]

        if dic["description"] is None:
            dic["description"] = survey["fields"]["description"]

        if dic["contents"] is None:
            dic["contents"] = survey["fields"]["contents"]

        original_survey.update(
            title=dic["title"],
            description=dic["description"],
            contents=dic["contents"],
            updated_datetime=datetime.datetime.now(),
        )

        return utils.send_json(responses.modifySurveySucceed)

    def delete(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)


# /surveys/{survey_id}/end
class SurveyEndView(View):
    def get(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def post(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def put(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=survey_id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)

        # result 필드 추가 및 response를 위한 클로저 함수
        def generate_result(result):
            survey_result = utils.to_dict(survey)[0]["fields"]
            result["result"] = survey_result
            return utils.send_json(result)

        if survey[0].status != "editing":
            return generate_result(responses.surveyAlreadyEnd)

        # editing 상황에서 처음으로 end api를 호출하는 경우 status 값 업데이트
        status = "published"
        survey.update(status=status, updated_datetime=datetime.datetime.now())
        return generate_result(responses.ok)

    def delete(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)
