from models.jwttoken import  get_current_user
from fastapi import APIRouter, Depends
from models.model import (User)
from database.database import *

ganime_router = APIRouter()

@ganime_router.get('/{judul_anime}')
def get_game_by_anime(judul_anime:str, current_user:User = Depends(get_current_user)):
    genre_anime =  get_anime_genre(judul_anime)
    return get_three_game_by_genre(genre_anime)
    