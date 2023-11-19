from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


@method_decorator(csrf_exempt, name='dispatch')
class TestView(View):
    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode()
        body = json.loads(body_unicode)
        return JsonResponse(body, safe=False)
