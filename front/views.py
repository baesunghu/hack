from django.utils.timezone import now
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .main import get_distance1
from .graphmaker import graphmaker
from django.utils import timezone
import json

# 아래 get_distance 함수는 본인의 API 키와 로직에 맞게 수정하세요.

from django.http import JsonResponse
import json


@csrf_exempt
def save_var(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        js_var = data.get('myVar')
        print(f"JavaScript에서 받은 값: {js_var}")
        v1, v2 = js_var.split(" ")
        graphmaker(float(v1), float(v2))
        return JsonResponse({'status': 'ok'})


def get_distance(loc1, loc2):
    # 예시: 실제로는 API 호출 코드 또는 내부 로직을 넣으세요
    # 여기선 임시로 두 역 이름 길이 합을 거리로 반환
    return get_distance1(loc1, loc2)


def index(request):
    return render(request, 'index.html', {'timestamp': now().timestamp()})


@csrf_exempt  # POST AJAX 요청 시 CSRF 문제 회피 (개발 단계)
def api_get_distance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            start_station = data.get('start_station')
            end_station = data.get('end_station')

            if not start_station or not end_station:
                return JsonResponse({'error': '출발역과 도착역을 모두 입력해주세요.'}, status=400)

            distance = get_distance(start_station, end_station)

            return JsonResponse({'distance': distance})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'POST 요청만 허용됩니다.'}, status=405)
