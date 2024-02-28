from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json
from django.http import JsonResponse

API_KEY = 'dhp3p74w6vmw9zdh'

@api_view(['GET'])
def places(request):
    try:
        url = 'https://api.visitjeju.net/vsjApi/contents/searchList'
        params = {
            'apiKey': API_KEY,
            'locale': 'kr',
            'category': 'c1'
        }
        response = requests.get(url, params=params)
        places_data = response.json()

        filtered_data = []
        print(len(places_data['items']))
        for item in places_data['items']:
            if "반려동물" in item["alltag"]:
                filtered_data.append(item)
            # 필터링된 데이터 반환
        return JsonResponse(filtered_data, safe=False, json_dumps_params={'ensure_ascii': False})

        # print(len(places_data["items"]))
        # return Response(places_data)

    except requests.RequestException as e:
        # API 호출 실패 시 에러 메시지 반환
        return JsonResponse({'error': str(e)}, status=500)
    
    return Response(places_data)