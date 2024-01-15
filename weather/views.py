from django.shortcuts import render
from .forms import CityForm
from .models import City
import requests

# def weather(request):
#     api_key = 'f31a6f95-9b8b-4fab-bcff-fd396c25612b'
#     url = 'https://api.weather.yandex.ru/v2/informers?lat=44.228376&lon=42.048277'
#
#
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             city_name = form.cleaned_data['name']
#             response = requests.get(url, headers={'X-Yandex-API-Key': api_key})
#             data = response.json()
#             return render(request, 'weather/json_page.html', {'data': data})
#
#             return render(request, 'weather/index.html', {'data': data})
#
#     else:
#         form = CityForm()
#
#     return render(request, 'weather/index.html',{'form': form})

def weather(request):
    api_key = 'Ваш token'
    url = 'https://api.weather.yandex.ru/v2/forecast'

    params={
        'lat': 44.228376,
        'lon': 42.048277,
        'lang': 'ru_RU',
    }

    response = requests.get(url, params=params, headers={'X-Yandex-API-Key': api_key})
    if response.status_code == 200:
        data = response.json()
        print(data)
        return render(request, 'weather/index.html', {'data': data})
    else:
        print(f"Ошибка при запросе: {response.status_code}")