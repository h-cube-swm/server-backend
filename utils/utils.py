from django.http import HttpResponse
from django.core.serializers import serialize
from urllib import parse
import json


# 딕셔너리를 JSON으로 전송하는 헬퍼 함수
def send_json(data):
    res = json.dumps(data)
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


# request.body로 받아왔을때 x-www-form-urlencoded를 dict로 변환하는 함수
def byte_to_dict(data):
    body_list = data.decode("utf-8").replace("&", "=").split("=")
    body_key = []
    body_value = []
    conv = lambda i: i or None
    for i in range(len(body_list)):
        if i % 2 == 0:
            body_key.append(body_list[i])
        else:
            body_value.append(conv(parse.unquote(body_list[i])))
    dict_body = dict(zip(body_key, body_value))
    return dict_body
