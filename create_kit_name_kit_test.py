import data
import sender_stand_request

# Тестовые значения для проверок №2 и №4
symbol511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

def get_new_user_token():
    user_responce = sender_stand_request.post_new_user (data.user_body)
    auth_token = user_responce.json()["authToken"]
    return auth_token

# Функция для изменения значения в параметре name в теле запроса для тестов
def get_kit_body (name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def positive_assert_201 (name):
    kit_body = get_kit_body (name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit (kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert_400 (name):
    kit_body = get_kit_body (name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit (kit_body, auth_token)
    assert kit_response.status_code == 400

def negative_assert_no_name (kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit (kit_body, auth_token)
    assert kit_response.status_code == 400

# Тест №1. Позитивная проверка. Параметр тame состоит из 1 символа.
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert_201 ("a")

# Тест №2. Позитивная проверка. Параметр тame состоит из 511 символов.
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assert_201 (symbol511)

# Тест №3. Негативная проверка. Параметр тame пустой.
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_400 ("")

# Тест №4. Негативная проверка. Параметр тame состоит из 512 символов.
def test_create_kit_512_symbols_in_name_get_error_response():
    negative_assert_400 (symbol512)

# Тест №5. Позитивная проверка. Параметр тame состоит из английских букв.
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert_201 ("QWErty")

# Тест №6. Позитивная проверка. Параметр тame состоит из русских букв.
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert_201 ("Мария")

# Тест №7. Позитивная проверка. Параметр тame состоит из спецсимволов.
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert_201 ("\"№%@\",")

# Тест №8. Позитивная проверка. В параметре тame есть пробелы.
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert_201 ("Человек и КО")

# Тест №9. Позитивная проверка. Параметр тame состоит из цифр.
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert_201 ("123")

# Тест №10. Негативная проверка. Параметр тame не передан в запросе.
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop ("name")
    negative_assert_no_name (kit_body)

# Тест №11. Негативная проверка. Параметр тame передан как число.
def test_create_kit_numeric_type_in_name_get_error_response():
    negative_assert_400 (123)