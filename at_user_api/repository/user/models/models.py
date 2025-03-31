from pydantic import BaseModel, EmailStr


class UserDB(BaseModel):
    id: int
    login: str
    password: str
    email: EmailStr
    group: str
