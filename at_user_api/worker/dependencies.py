from typing import Protocol

from at_user_api.service.user.service import UserService


class IUserService(Protocol):
    def verify_token(self, token: str) -> int: ...

_: IUserService = UserService(...)  # type: ignore[arg-type, reportArgumentType]
