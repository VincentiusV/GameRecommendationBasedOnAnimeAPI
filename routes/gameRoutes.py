from models.jwttoken import create_access_token, get_current_user
# from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Body, HTTPException, Depends, Request,status
# from models.hashing import Hash
from models.model import (User, Login, Token, TokenData,game_schema, update_game_schema)
# from database.database import get_game_by_genre, get_game_by_judul, user_db,get_all_games, get_game_by_id, add_game, update_game, delete_game, game_parser, games_serializer, games_col, games_test
from database.database import *
import sys
from fastapi.encoders import jsonable_encoder

game_router = APIRouter()
sys.setrecursionlimit(100000)

# current_user:User = Depends(get_current_user)

# Read
@game_router.get('/')
def get_all_game(current_user:User = Depends(get_current_user)):
    games = get_all_games()
    if games:
        return games
    return ("No games found")

# @game_router.get('/{judul_game}')
# def get_game_by_judul(judul_game: str):
#     game_by_judul = {"judul_game": {"$regex": judul_game.capitalize()}}
#     return games_serializer(games_col.find(game_by_judul))

@game_router.get('/get-game-by-id/{id}')
async def get_game_data_by_id(id, current_user:User = Depends(get_current_user)):
    game = await get_game_by_id(id)
    if game:
        return game
    return ("No games found")

@game_router.get('/get-game-by-judul/{judul_game}')
def get_game_data_by_judul(judul_game: str):
    game = get_game_by_judul(judul_game)
    if game :
        return game
    return ("No games found")

@game_router.get('/get-game-by-genre/{genre_game}')
def get_game_data_by_genre(genre_game: str):
    game = get_game_by_genre(genre_game)
    if game :
        return game
    return ("No games found")

# Create
@game_router.post('/add')
async def add_game_data(game: game_schema = Body(...), current_user:User = Depends(get_current_user)):
    game = jsonable_encoder(game)
    new_game = await add_game (game)
    return (new_game)

# Update
@game_router.put('/update/{id}')
async def update_game_data(id: str, game: update_game_schema = Body(...), current_user:User = Depends(get_current_user)):
    game = {k: v for k, v in game.dict().items() if v is not None}
    updated_game = await update_game(id, game)
    if updated_game :
        return (updated_game)
    return ("There was an error updating the game")

# Delete
@game_router.delete('/delete/{id}')
async def delete_game_data(id: str, current_user:User = Depends(get_current_user)):
    deleted_game = await delete_game(id)
    if deleted_game :
        return ("Game deleted successfully")
    return ("There was an error deleting the game")