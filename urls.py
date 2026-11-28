class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    # Ингредиенты
    INGREDIENTS = f"{BASE_URL}/ingredients"

    # Пользователь
    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    LOGOUT = f"{BASE_URL}/auth/logout"
    TOKEN = f"{BASE_URL}/auth/token"
    USER = f"{BASE_URL}/auth/user"

    # Заказы
    ORDERS = f"{BASE_URL}/orders"
    ORDERS_ALL = f"{BASE_URL}/orders/all"

    # Пароль
    PASSWORD_RESET = f"{BASE_URL}/password-reset"
    PASSWORD_RESET_RESET = f"{BASE_URL}/password-reset/reset"
