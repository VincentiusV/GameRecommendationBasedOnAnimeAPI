from models.jwttoken import get_current_user
from fastapi import APIRouter, Depends
from models.model import User
from database.database import *
from database.gamespecs import get_spec
from routes.accessAPI import get_structure

gamespecs_router = APIRouter()

#Get Game Specs
@gamespecs_router.get('/get-specs/{judul_game}')
def get_game_simple_spec(judul_game: str, current_user:User = Depends(get_current_user)):
    game_spec = get_spec(judul_game)
    if game_spec:
        return game_spec.title()
    return ("No games found")

@gamespecs_router.get('/recommended-specs/{judul_game}')
def get_recommended_pc_specs(judul_game: str, current_user:User = Depends(get_current_user)):
    spec_game = get_spec(judul_game)
    spec_game = spec_game.title().replace(" ", "%20")
    url = f'https://tubeststwid.azurewebsites.net/core/list_recommendation/game/{spec_game}'
    return get_structure(url)