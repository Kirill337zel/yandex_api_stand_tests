﻿# Тесты на проверку параметра firstName при создании пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
﻿# Тесты на проверку параметра name при создании набора у авторизованного пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
Для запуска тестов должны быть установлены пакеты pytest и requests
Запуск всех тестов выполянется командой pytest create_kit_name_kit_test.py
Все тесты разбиты на негативные проверки и позитивные
Позитивные проверки проверяют код ответа 201 и совпадает ли поле name в запросе с полем name в ответе
Негативные проверки проверяют только код ответа 400
При отправке запроса передается "authToken" в headers
authToken генерируется каждый раз при прохождении тестов с помощью отдельной функции get_new_user_token()
Функция get_new_user_token() создает нового пользователя и возвращает authToken
