from models.jwttoken import create_access_token, get_current_user
from fastapi import APIRouter, Body, Depends
from models.model import (User, Login, Token, TokenData,game_schema, update_game_schema)
from database.database import *
from database.gamespecs import get_spec
import sys
from fastapi.encoders import jsonable_encoder

gamespecs_router = APIRouter()

#Get Game Specs
@gamespecs_router.get('/get-specs/{judul_game}')
def get_game_simple_spec(judul_game: str, current_user:User = Depends(get_current_user)):
    game_spec = get_spec(judul_game)
    if game_spec:
        return game_spec
    return ("No games found")