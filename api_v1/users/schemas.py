from pydantic import ConfigDict
from pydantic import BaseModel
from pydantic import EmailStr



class UserBase(BaseModel):

    username: str


class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):

    name: str | None = None
    description: str | None = None
    count: int | None = None
    price: int | None = None