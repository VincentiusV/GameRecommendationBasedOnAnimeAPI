from pymongo import MongoClient
from models.model import game_schema
from bson.objectid import ObjectId

mongodb_uri = 'mongodb+srv://admin:admin@clustertst.92xxsyc.mongodb.net/?retryWrites=true&w=majority'
port = 8000
client = MongoClient(mongodb_uri, port)

user_db = client["User"]

game_db = client["Game"]
games_col = game_db["games"]
games_test = game_db['gametest']

# Parser from Mongo to Python
def game_parser(game) -> dict:
    return {
        "id": str(game["_id"]),
        "judul_game": game["judul_game"],
        "tahun_pembuatan": game["tahun_pembuatan"],
        "genre": game["genre"],
        "developer": game["developer"],
    }

# def games_serializer(games) -> dict:
#     return [game_parser(game) for game in games]

# Retrieve all games
def get_all_games():
    games = []
    for game in games_col.find():
        games.append(game_parser(game))
    return games

# Retrieve a game by name
# def get_game_by_name(judul_game: str) -> dict:
#     game = games_serializer(games_test.find({"judul_game": judul_game}))
#     if game:
#         return game_parser(game)

# Retrieve a game by id
async def get_game_by_id(id: str) -> dict:
    game = games_col.find_one({"_id": ObjectId(id)})
    if game:
        return game_parser(game)

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