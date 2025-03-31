from at_user_api.delivery.auth.models.models import SignUpRequest
from at_user_api.repository.user.models.models import UserDB


def to_UserDB(user: SignUpRequest) -> UserDB:
    return UserDB(
        id=0,
        login=user.login,
        password=user.password,
        email=user.email,
        group=user.group,
    )
