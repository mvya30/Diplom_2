# Diplom_2:
1) Создание пользователя (TestCreateUser):
 1. test_create_unique_user_success - Успешная регистрация уникального пользователя
 2. test_create_duplicate_user - Попытка зарегистрировать уже существующего пользователя
 3. test_create_user_no_email - Регистрация без поля email
 4. test_create_user_no_password - Регистрация без поля password
 5. test_create_user_no_name - Регистрация без поля name

2) Логин пользователя (TestLoginUser)
 1. test_login_ok - Вход под существующим пользователем с корректными данными
 2. test_login_wrong_email - Вход с неверным логином (email) и верным паролем
 3. test_login_wrong_password - Вход с верным логином и неверным паролем
 5. test_login_wrong_credentials - Вход с неверными логином и паролем одновременно

3) Создание заказа (TestCreateOrder):
 1. test_order_with_auth - Создание заказа авторизованным пользователем с ингредиентами
 2. test_order_without_auth - Создание заказа без авторизации с ингредиентами
 3. test_order_with_ingredients - Создание заказа с ингредиентами: проверка структуры ответа
 4. test_order_without_ingredients - Создание заказа с пустым списком ингредиентов
 5. test_order_bad_hash - Создание заказа с неверным хешем ингредиента