import requests

# Задаем координаты населенного пункта
lat = 55.75396  # широта Москвы
lon = 37.620393  # долгота Москвы

# Задаем параметры запроса
params = {
    'lat': lat,
    'lon': lon,
    'lang': 'ru_RU',  # язык ответа
    'limit': 7,  # срок прогноза в днях
    'hours': True,  # наличие почасового прогноза
    'extra': False  # подробный прогноз осадков
}

# Задаем значение ключа API
api_key = 'f31a6f95-9b8b-4fab-bcff-fd396c25612b'

# Задаем URL API
url = 'https://api.weather.yandex.ru/v2/forecast'

# Делаем запрос к API
response = requests.get(url, params=params, headers={'X-Yandex-API-Key': api_key})

# Проверяем статус ответа
if response.status_code == 200:
    # Преобразуем ответ в JSON формат
    data = response.json()
    # Выводим данные о текущей погоде
    print(f'Температура воздуха: {data["fact"]["temp"]} °C')
    print(f'Ощущается как: {data["fact"]["feels_like"]} °C')
    print(f'Скорость ветра: {data["fact"]["wind_speed"]} м/с')
    print(f'Давление: {data["fact"]["pressure_mm"]} мм рт. ст.')
    print(f'Влажность: {data["fact"]["humidity"]} %')
    print(f'Погодное описание: {data["fact"]["condition"]}')
else:
    # Выводим код ошибки
    print(f'Ошибка: {response.status_code}')