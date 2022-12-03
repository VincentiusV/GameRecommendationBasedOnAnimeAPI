from pymongo import MongoClient
from models.model import game_schema

mongodb_uri = 'mongodb+srv://admin:admin@clustertst.92xxsyc.mongodb.net/?retryWrites=true&w=majority'
port = 8000
client = MongoClient(mongodb_uri, port)

user_db = client["User"]

game_db = client["Game"]
games_col = game_db["games"]

# Parser from Mongo to Python
def game_parser(game) -> dict:
    return {
        "id": str(game["_id"]),
        "judul_game": game["judul_game"],
        "tahun_pembuatan": game["tahun_pembuatan"],
        "genre": game["genre"],
        "developer": game["developer"],
    }

def games_serializer(games) -> dict:
    return [game_parser(game) for game in games]

# Retrieve all games
def get_all_games():
    games = []
    for game in games_col.find():
        games.append(game_parser(game))
    return games

# Retrieve a game by name
def get_game_by_name(judul_game: str) -> dict:
    game = games_serializer(games_col.find({"judul_game": judul_game}))
    if game:
        return game_parser(game)
