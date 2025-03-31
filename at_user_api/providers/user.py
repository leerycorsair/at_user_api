from fastapi import Depends
from sqlalchemy.orm import Session

from at_user_api.repository.user.repository import UserRepository
from at_user_api.service.user.service import UserService
from at_user_api.storage.postgres.session import get_db


def get_user_repository(session: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(session)


def get_user_service(user_rep=Depends(get_user_repository)) -> UserService:
    return UserService(user_rep)
