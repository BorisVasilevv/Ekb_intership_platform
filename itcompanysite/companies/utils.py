import re
import requests
import environ

env = environ.Env()
environ.Env.read_env()



def has_russian_letters(input_string):
    if input_string is None:
        return False

    russian_letters_pattern = re.compile('[а-яА-Я]')
    return bool(russian_letters_pattern.search(input_string))


def geocoder(address):
    url = "https://api.geotree.ru/address.php"
    parameters = {'key': env('GEO_KEY'), "term": address}

    response = requests.get(url, params=parameters)

    # проверяем успешность запроса
    if response.status_code == 200:
        # получаем JSON-ответ
        json_response = response.json()

        # доступ к координатам
        try:
            first_result = json_response[0]
            geo_center = first_result['geo_center']
            latitude = geo_center['lat']
            longitude = geo_center['lon']
            coordinates = [latitude, longitude]

            return coordinates

        except (IndexError, KeyError) as e:
            print(f"Ошибка при извлечении координат: {e}")
            return None
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return None
