from pymongo import MongoClient
# from models.model import game_schema
from bson.objectid import ObjectId
import re
import json

mongodb_uri = 'mongodb+srv://admin:admin@clustertst.92xxsyc.mongodb.net/?retryWrites=true&w=majority'
port = 8000
client = MongoClient(mongodb_uri, port)

user_db = client["User"]

game_db = client["Game"]
games_col = game_db["games"]
games_test = game_db['gametest']

anime_db = client["Anime"]
anime_col = anime_db["anime"]

# Parser from Mongo to Python
def game_parser(game) -> dict:
    return {
        "id": str(game["_id"]),
        "judul_game": game["judul_game"],
        "tahun_pembuatan": game["tahun_pembuatan"],
        "genre": game["genre"],
        "developer": game["developer"]
    }

def anime_parser(anime) -> dict:
    return {
        "id": str(anime["_id"]),
        "judul_anime": anime["judul_anime"],
        "genre_anime": anime["genre_anime"]
    }

def games_serializer(games) -> list:
    return [game_parser(game) for game in games]

def anime_serializer(animes) -> list:
    return [anime_parser(anime) for anime in animes]

# Retrieve all games
def get_all_games():
    games = []
    for game in games_col.find():
        games.append(game_parser(game))
    return {"Total Games" : len(games)}, games

# Retrieve a game by id
async def get_game_by_id(id: str) -> dict:
    game = games_col.find_one({"_id": ObjectId(id)})
    if game:
        return game_parser(game)

# Retrieve a game by judul
def get_game_by_judul(judul_game: str):
    game_by_judul = {"judul_game": {"$regex": judul_game.title()}}
    return games_serializer(games_col.find(game_by_judul))

# def get_game_by_judul(game_name: str):
#     games = []
#     search = game_name.title().split()
#     for game in games_col.find():
#         if all(x in game['judul_game'] for x in search):
#             games.append(game_parser(game))
#     return games

# Retrieve games by genre
def get_game_by_genre(genre: str):
    game_by_genre = {"genre": {"$regex": genre.capitalize()}}
    return games_serializer(games_col.find(game_by_genre))

# Add Game
async def add_game(game: dict) -> dict:
    game = games_col.insert_one(game)
    new_game = games_col.find_one({"_id": game.inserted_id})
    return game_parser(new_game)

# Update Game
async def update_game(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    game = games_col.find_one({"_id": ObjectId(id)})

    if game:
        updated_game = games_col.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_game:
            return True
        return False

# Delete Game
async def delete_game(id: str):
    game = games_col.find_one({"_id": ObjectId(id)})
    if game:
        games_col.delete_one({"_id": ObjectId(id)})
        return True

# Get Anime Genre
def get_anime_genre(judul_anime:str):
    anime = {"judul_anime": {"$regex": judul_anime.capitalize()}}
    anime_data = (anime_col.find_one(anime))
    # anime_data_extracted = json.loads(anime_data)
    return (anime_data['genre_anime'])

# Get One Random Game
def get_one_game_by_genre(genre: str):
    game_by_genre = {"genre": {"$regex": genre.capitalize()}}
    return (games_col.find_one(game_by_genre, {'_id': 0}))


