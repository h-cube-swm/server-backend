from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import User
from utils import utils, responses

# Create your views here.


class RootView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        result = responses.postOnly
        return utils.send_json(result)

    def post(self, request: HttpRequest) -> HttpResponse:
        keys = ["uid"]
        dic = utils.pop_args(request.POST, *keys)

        if None in list(dic.values()):
            return utils.send_json(responses.illegalArgument)

        filtered = User.objects.filter(uid=dic["uid"])
        if filtered.count():
            return utils.send_json(responses.userAlreadyRegistered)

        user_type = {"IDENTIFIER": "pre", "EMAIL": "basic"}
        # uid 분기 처리
        uid_type = utils.validate_uid(dic["uid"])

        # uid 타입이 IDENTIFIER도 EMAIL도 아닐 경우
        if not uid_type:
            return utils.send_json(responses.illegalUID)
        user_type = user_type.get(uid_type)

        # 유저 생성
        User.objects.create(uid=dic["uid"], user_type=user_type)
        result = responses.createUserSucceed
        return utils.send_json(result)


class ElementView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass

    def delete(self, request: HttpRequest, pk: int) -> HttpResponse:
        pass
