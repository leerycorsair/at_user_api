from at_user_api.repository.user.models.models import UserDB
from at_user_api.schema.user import User


def to_User(user: UserDB) -> User:
    return User(
        login=user.login,
        password=user.password,
        email=user.email,
        group=user.group,
    )


def to_UserDB(user: User) -> UserDB:
    return UserDB(
        id=user.id,
        login=user.login,
        password=user.password,
        email=user.email,
        group=user.group,
    )
