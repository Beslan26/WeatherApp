from django.shortcuts import render
import requests


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