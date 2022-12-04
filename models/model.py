from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    username: str
    password: str
class Login(BaseModel):
	username: str
	password: str
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: Optional[str] = None

class game_schema(BaseModel):
    judul_game : str = Field(...)
    tahun_pembuatan : str = Field(...)
    genre : str = Field(...)
    developer : str = Field(...)
class update_game_schema(BaseModel):
    judul_game : Optional[str]
    tahun_pembuatan : Optional[str]
    genre : Optional[str]
    developer : Optional[str]
