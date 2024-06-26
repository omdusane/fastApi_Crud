from pydantic import BaseModel
from typing import List, Union


class TodoBase(BaseModel):
    title: str
    status: str 
    
class Todo(TodoBase):
    class Config():
        orm_mode=True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    todos: List[Todo] = []

    class Config():
        orm_mode=True

class ShowUserBasic(BaseModel):
    name:str
    class Config():
        orm_mode=True

class ShowTodo(BaseModel):
    title: str
    status: str
    creator: ShowUserBasic
    class Config():
        orm_mode=True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None