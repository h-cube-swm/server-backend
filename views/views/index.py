from django.views import View
from utils import utils, responses

# Create your views here.


class IndexView(View):
    def get(self, request):
        return utils.send_json(responses.APIOnly)

    def post(self, request):
        return self.get(request)
