from models.jwttoken import  get_current_user
from fastapi import APIRouter, Body, Depends
from models.model import (User, game_schema, update_game_schema)
# from database.database import get_game_by_genre, get_anime_genre
from database.database import *
from fastapi.encoders import jsonable_encoder

ganime_router = APIRouter()

@ganime_router.get('/{judul_anime}')
def get_game_by_anime(judul_anime:str):
    genre_anime = get_anime_genre(judul_anime)
    return get_one_game_by_genre(genre_anime)
