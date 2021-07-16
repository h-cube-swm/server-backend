from django.http import HttpResponse, HttpRequest
from django.views import View
from utils import utils, responses

# Create your views here.


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return utils.send_json(responses.APIOnly)

    def post(self, request: HttpRequest) -> HttpResponse:
        return self.get(request)
