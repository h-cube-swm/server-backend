from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest
from django.views import View
from surveys.models import Survey
from utils import utils, responses
from django.utils import timezone
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import requests
from decouple import config

# Create your views here.


def send_email(user_email, survey_model: QuerySet):
    survey_model = survey_model[0]
    user_email = user_email
    title = survey_model.title
    survey_link = survey_model.survey_link
    response_link = survey_model.response_link

    subject = f"더 폼에서 작성하신 <{title}> 설문에 대한 정보입니다."
    from_email = "<support@the-form.io>"
    to = [user_email]

    html_message = render_to_string(
        "mail.html",
        {
            "title": title,
            "survey_link": response_link,
            "result_link": survey_link,
        },
    )
    plain_message = strip_tags(html_message)

    msg = EmailMultiAlternatives(
        subject=subject, body=plain_message, from_email=from_email, to=to
    )
    msg.attach_alternative(html_message, "text/html")
    msg.content_subtype = "html"
    msg.mixed_subtype = "related"

    try:
        msg.send()
    except Exception as e:
        print("메일 송신 중 에러가 발생 했습니다", e)
        # 만약 전송 실패했을시 mailgun 활용
        response = requests.post(
            "https://api.mailgun.net/v3/the-form.io/messages",
            auth=("api", config("MAILGUN_API_KEY")),
            data={
                "from": "<support@the-form.io>",
                "to": [user_email],
                "subject": f"더 폼에서 작성하신 <{title}> 설문에 대한 정보입니다.",
                "html": render_to_string(
                    "mail.html",
                    {
                        "title": title,
                        "survey_link": response_link,
                        "result_link": survey_link,
                    },
                ),
            },
        )
        return response.status_code
    return 200


# /link
class LinkView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if not utils.is_the_form(request):
            return utils.send_json(responses.notAllowed)
        survey = Survey.objects.create()
        result = responses.ok.copy()
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
        if not utils.is_the_form(request):
            return utils.send_json(responses.notAllowed)

        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        # 설문이 요청될 때 설문 링크와 응답 링크를 둘 다 이용하여 검색한다.
        survey = Survey.objects.filter(
            Q(survey_link=survey_id) | Q(response_link=survey_id)
        )

        if survey.count() == 0:
            return utils.send_json(responses.invalidSurveyID)

        # 설마 UUID 가 겹치지는 않겠지만, 혹시 모르니까 Assert를 걸어준다.
        assert survey.count() == 1

        survey = utils.to_dict(survey)[0]["fields"]
        result = responses.ok.copy()
        result["result"] = survey
        return utils.send_json(result)

    def post(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def put(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        if not utils.is_the_form(request):
            return utils.send_json(responses.notAllowed)

        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=survey_id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)
        if survey[0].status != "editing":
            return utils.send_json(responses.surveyCannotEdit)

        request_dict = utils.json_to_dict(request.body)

        # request.body에서 딕셔너리 추출
        body_keys = ["title", "description", "contents"]
        dic = utils.pop_args(request_dict, *body_keys)

        # 위 파라미터 중 1개라도 담겨서 오지 않는 경우
        if [None] * len(body_keys) == list(dic.values()):
            return utils.send_json(responses.illegalArgument)

        original_survey = survey
        survey = utils.to_dict(survey)[0]

        # 데이터베이스 update가 문제 없게 동작하기 위한 분기 처리
        # ToDo : 최신 문법에서 간단하게 처리 가능할 것임. 자바스크립트 전개연산자처럼 사용가능한 걸로 암.
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
            updated_datetime=timezone.now(),
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
        if not utils.is_the_form(request):
            return utils.send_json(responses.notAllowed)

        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=survey_id)
        if survey.count() == 0:
            return utils.send_json(responses.invalidSurveyID)

        # result 필드 추가 및 response를 위한 클로저 함수
        def generate_result(result):
            survey_result = utils.to_dict(survey)[0]["fields"]
            result["result"] = survey_result
            return utils.send_json(result)

        # editing 상황에서 처음으로 end api를 호출하는 경우 status 값 업데이트
        status = "published"
        survey.update(status=status, updated_datetime=timezone.now())

        return generate_result(responses.ok.copy())

    def delete(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)


# /surveys/{survey_id}/emails
class SurveyEmailView(View):
    def get(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def post(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)

    def put(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        if not utils.is_the_form(request):
            return utils.send_json(responses.notAllowed)

        if not utils.is_valid_uuid(survey_id):
            return utils.send_json(responses.invalidUUID)

        survey = Survey.objects.filter(survey_link=survey_id)
        if not survey.count():
            return utils.send_json(responses.invalidSurveyID)

        if not request.body:
            return utils.send_json(responses.illegalArgument)

        request_dict = utils.json_to_dict(request.body)

        # request.body에서 딕셔너리 추출
        body_keys = ["email"]
        dic = utils.pop_args(request_dict, *body_keys)

        if not utils.is_valid_email(dic["email"]):
            return utils.send_json(responses.noEmail)

        user_email = dic["email"]
        survey.update(user_email=user_email)

        # aws ses를 통한 메일 송신
        response = send_email(user_email, survey)
        if response == 200:
            return utils.send_json(responses.ok)

        return utils.send_json(responses.emailError)

    def delete(self, request: HttpRequest, survey_id: str) -> HttpResponse:
        return utils.send_json(responses.noAPI)
