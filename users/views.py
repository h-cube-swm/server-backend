from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import User
from utils import utils, responses

import logging

logger = logging.getLogger(__name__)
# Create your views here.


class RootView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if "token" not in request.GET:
            return utils.send_json(responses.tokenRequired)
        token = request.GET["token"]
        user_id = utils.decode_token(token)
        if user_id is None:
            return utils.send_json(responses.invalidToken)

        user = User.objects.filter(id=user_id)
        if not user.count():
            return utils.send_json(responses.noUser)

        user = utils.to_dict(user)[0]
        result = responses.ok
        result["result"] = user
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
            return utils.send_json(responses.invalidUID)
        user_type = user_type.get(uid_type)

        # 유저 생성
        User.objects.create(uid=dic["uid"], user_type=user_type)
        result = responses.createUserSucceed
        return utils.send_json(result)


class ElementView(View):
    def get(self, request: HttpRequest, user_pk: int) -> HttpResponse:
        pass

    def put(self, request: HttpRequest, user_pk: int) -> HttpResponse:
        pass

    def delete(self, request: HttpRequest, user_pk: int) -> HttpResponse:
        keys = ["token"]
        request_dict = utils.byte_to_dict(request.body)
        dic = utils.pop_args(request_dict, *keys)

        if None in list(dic.values()):
            return utils.send_json(responses.illegalArgument)

        token = dic["token"]
        user_id = utils.decode_token(token)
        if user_id is None:
            return utils.send_json(responses.invalidToken)

        # authorization 추후 데코레이터 기반으로 리팩토링 예정
        if user_pk != user_id:
            return utils.send_json(responses.notAuthorized)

        user = User.objects.filter(id=user_id)
        if not user.count():
            return utils.send_json(responses.noUser)

        # 유저 삭제
        user.delete()
        result = responses.deleteUserSucceed
        return utils.send_json(result)
