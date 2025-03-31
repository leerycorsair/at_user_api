from fastapi import APIRouter, Depends, HTTPException

from at_user_api.delivery.user.dependencies import IUserService
from at_user_api.delivery.user.models.conversions import to_UserDB
from at_user_api.delivery.user.models.models import (
    SignInRequest,
    SignInResponse,
    SignUpRequest,
    SignUpResponse,
)
from at_user_api.providers.user import get_user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/sign_in", response_model=SignInResponse)
async def sign_in(
    body: SignInRequest,
    user_service: IUserService = Depends(get_user_service),
):
    try:
        token = user_service.generate_token(
            body.login,
            body.password,
        )
    except ValueError:
        raise HTTPException(status_code=401, detail="Login failed")
    return SignInResponse(token=token)


@router.post("/sign_up", response_model=SignUpResponse)
async def sign_up(
    body: SignUpRequest,
    user_service: IUserService = Depends(get_user_service),
):
    user_id = user_service.create_user(to_UserDB(body))
    return SignUpResponse(user_id=user_id)
