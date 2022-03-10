from enum import Enum


class Roles(str, Enum):
    STUDENT = "Student"
    ADMIN = "Admin"
    LECTURER = "lecturer"


