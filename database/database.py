from pymongo import MongoClient

mongodb_uri = 'mongodb+srv://admin:admin@clustertst.92xxsyc.mongodb.net/?retryWrites=true&w=majority'
port = 8000
client = MongoClient(mongodb_uri, port)

user_db = client["User"]
game_db = client["Game"]