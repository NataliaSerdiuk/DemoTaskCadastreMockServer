from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from random import choice
import time


@csrf_exempt
@require_POST
def result_query(request):
    data = request.POST
    cadastre_number = data.get('cadastre_number')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Эмулированная логика ответа(например,относится ли земельный участок к землям сельхозназначения или нет)
    response_query = choice([True, False])
    result_dict = {'response': response_query}
    return JsonResponse(result_dict)

@csrf_exempt
@require_GET
def check(request):     # Проверка запуска сервера
    return JsonResponse({'message': "Check"})