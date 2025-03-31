from at_user_api.dto.db.user import UserDB


class UserRepositoryInterface:
    def create_user(self, user: UserDB) -> int:
        pass

    def get_user(self, login: str) -> UserDB:
        pass
