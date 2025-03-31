from typing import Protocol

from at_user_api.repository.user.models.models import UserDB


class IUserRepository(Protocol):
    def create_user(self, user: UserDB) -> int: ...

    def get_user(self, login: str) -> UserDB: ...
