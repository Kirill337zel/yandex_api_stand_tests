# Импортируем необходимые библиотеки и модули
import requests
import configuration
import data

# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get (configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Запрос на создание нового пользователя
def post_new_user (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers = data.headers)

# Создание личного набора для этого пользователя
def post_new_client_kit(kit_body,auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KITS_PATH,
                         json = kit_body,
                         headers = auth_headers)