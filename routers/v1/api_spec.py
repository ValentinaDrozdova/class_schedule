from enum import Enum


class ApiSpec(str, Enum):
    LOGIN = "/login"

    USERS = "/users"
    USERS_DETAIL = "/users/{user_id}"
    