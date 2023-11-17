import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        username_regex = '^[a-z]{3,}$'
        password_regex = '^(?=.*[0-9!@#$%^&*()_+={}\[\]:;<>,.?~\\-])[a-zA-Z0-9!@#$%^&*()_+={}\[\]:;<>,.?~\\-]{8,}$'

        is_username_valid = bool(re.match(username_regex, username))
        is_password_valid = bool(re.match(password_regex, password))

        if is_username_valid is False:
            raise UserInputError("Username should be at least 3 characters long and only contain letters a-z.")
        
        if is_password_valid is False:
            raise UserInputError("Password should be at least 8 characters long and contain special symbols and/or numbers.")