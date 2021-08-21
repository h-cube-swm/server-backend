from django.http import HttpResponse
from django.core.serializers import serialize
from urllib import parse
from uuid import UUID
import json
from src.settings import DEBUG

ALLOWED_ORIGIN = ["https://the-form.io"]

# 요청한 origin이 the-form.io나 dev.the-form.io 프론트엔드인지 식별 - 임시
def is_origin_valid(request):
    if DEBUG:
        return True

    print(request.META)
    if "HTTP_ORIGIN" not in request.META:
        return False
    if request.META["HTTP_ORIGIN"] not in ALLOWED_ORIGIN:
        return False
    return True


# 이메일 유효성 검사 헬퍼 함수
def is_valid_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError

    try:
        validate_email(email)
        return True
    except ValidationError as e:
        print("bad email, details:", e)
        return False


# 딕셔너리를 JSON으로 전송하는 헬퍼 함수
def send_json(data):
    res = json.dumps(data, default=str)
    return HttpResponse(res, content_type="application/json", status=data["status"])


# 가변 인자로 추출된 딕셔너리를 받아오는 헬퍼 함수
def pop_args(dic, *args):
    return {arg: dic[arg] if arg in dic else None for arg in args}


# QuerySet 객체를 dict 객체로 변환하는 헬퍼 함수
def to_dict(queryset):
    return json.loads(serialize("json", queryset))


def pk_to_dict(objects, pk):
    return to_dict(objects.filter(pk=pk))


# request.body로 받아왔을때 json을 dict로 변환하는 함수
def json_to_dict(data):
    return json.loads(data.decode("utf-8"))


def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test
