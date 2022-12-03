from models.jwttoken import create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Depends, Request,status
from models.hashing import Hash
from models.model import (User, Login, Token, TokenData)
from database.database import user_db,get_all_games, get_game_by_name

game_router = APIRouter()

# current_user:User = Depends(get_current_user)

@game_router.get('/')
def get_all_game():
    games = get_all_games()
    if games:
        return games
    return ("No games found")

@game_router.get('/{judul_game}')
def get_game_by_judul(judul_game):
    game = get_game_by_name(judul_game)
    if game:
        return game
    return ("No games found")


