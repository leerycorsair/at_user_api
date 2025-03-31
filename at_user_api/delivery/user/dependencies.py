from typing import Protocol

from at_user_api.repository.user.models.models import UserDB


class IUserService(Protocol):
    def create_user(self, user: UserDB) -> int: ...

    def generate_token(self, login: str, password: str) -> str: ...
