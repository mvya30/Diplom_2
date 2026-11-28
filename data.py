class DataForUser:
    INVALID_LOGIN_DATA_1 = {
        "email": "nonexistent@example.com",
        "password": "password123",
    }
    INVALID_LOGIN_DATA_2 = {
        "email": "wrong_email@example.com",
        "password": "wrong_password",
    }
    INVALID_LOGIN_DATA_3 = {
        "email": "nonexistent@example.com",
        "password": "wrong_password",
    }

class Messages:
    WRONG_CREDENTIALS = "email or password are incorrect"
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    INGREDIENTS_REQUIRED = "Ingredient ids must be provided"