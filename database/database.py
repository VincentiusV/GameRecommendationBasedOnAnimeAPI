from pymongo import MongoClient
from bson.objectid import ObjectId
from random import *

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

# Retrieve games by genre
def get_game_by_genre(genre: str):
    game_by_genre = {"genre": {"$regex": genre.title()}}
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
    anime = {"judul_anime": {"$regex": judul_anime.title()}}
    anime_data = (anime_col.find_one(anime))
    # anime_data_extracted = json.loads(anime_data)
    return (anime_data['genre_anime'])

# Get Three Random Game based on Genre
def get_three_game_by_genre(genre: str):
    genre1 = genre_serializer(genre)
    temp = get_game_by_genre(genre1)
    list_random_game = []
    jumlah_game = len(temp)
    for _ in range(3):
        value = randint(0, jumlah_game)
        list_random_game.append(temp[value])
    return list_random_game

# Genre Serializer
def genre_serializer(genre: str):
    if genre == "Action" :
        genre_game = "Action"
    elif genre == "Comedy":
        genre_game = "Party"
    elif genre == "Horror":
        genre_game = "Survival Horror"
    elif genre == "Sports":
        genre_game = "Sports"
    elif genre == "Adventure":
        genre_game = "Adventure"
    elif genre == "Drama":
        genre_game = "Role-Playing Game"
    elif genre == "Mystery":
        genre_game = "Hidden Object"
    elif genre == "Supernatural":
        genre_game = "Survival Horror"
    elif genre == "Avant Garde":
        genre_game = "Simulation"
    elif genre == "Fantasy":
        genre_game = "Simulation"
    elif genre == "Romance":
        genre_game = "Life Simulation"
    elif genre == "Suspense":
        genre_game = "Casual"
    elif genre == "Award Winning":
        genre_game = "Party"
    elif genre == "Girls Love":
        genre_game = "Life Simulation"
    elif genre == "Sci-Fi":
        genre_game = "Adventure"
    elif genre == "Boys Love":
        genre_game = "Life Simulation"
    elif genre == "Gourmet":
        genre_game = "Roguelike"
    elif genre == "Slice of Life":
        genre_game = "Life Simulation"
    elif genre == "Ecchi":
        genre_game = "Life Simulation"
    elif genre == "Erotica":
        genre_game = "Life Simulation"
    elif genre == "Hentai":
        genre_game = "Life Simulation"
        
    return genre_game
