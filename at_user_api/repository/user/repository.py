from sqlalchemy.orm import Session

from at_user_api.repository.user.models.conversions import to_User, to_UserDB
from at_user_api.repository.user.models.models import UserDB
from at_user_api.schema.user import User


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, user: UserDB) -> int:
        new_user = to_User(user)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)

        return new_user.id

    def get_user(self, login: str) -> UserDB:
        user = self.db_session.query(User).filter_by(login=login).first()
        if user is not None:
            return to_UserDB(user)
        else:
            raise ValueError("User not found")
