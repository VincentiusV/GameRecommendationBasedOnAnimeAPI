from database import games_test, game_db
import json
import random

# def game_parser(game) -> dict:
#     return {
#         "id": str(game["_id"]),
#         "judul_game": game["judul_game"],
#         "tahun_pembuatan": game["tahun_pembuatan"],
#         "genre": game["genre"],
#         "developer": game["developer"]
#     }

# def games_serializer(games) -> list:
#     return [game_parser(game) for game in games]

# def get_game_by_judul(judul_game: str):
#     game_by_judul = {"judul_game": {"$regex": judul_game.capitalize()}}
#     return games_serializer(games_test.find(game_by_judul))

# print(get_game_by_judul("A Bird"))

# dictionary = {'Ram' : 14, 'Rahul' : 10, 'Raj' : 25, 'Preeti' : 43}

# print('The given dictionary is : ',games_test)
# # Converting iterable of the dictionary to a list
# list_of_entry = list(games_test.items())
# # Choosing a random entry from the list_of_entry
# random_entry = random.choice(list_of_entry)
# print('The random entry is :',random_entry)

# games_test.aggregate([{ $sample: { size: 1 } }])

cursor = game_db.gametest.aggregate([ { "$sample": { "size": 1 } } ])
for document in cursor:
    print(document)

# db.mycoll.aggregate([{ $sample: { size: 1 } }])

# def anime_parser(anime) -> dict:
#     return {
#         "id": str(anime["_id"]),
#         "judul_anime": anime["judul_anime"],
#         "genre_anime": anime["genre_anime"]
#     }

# def anime_serializer(animes) -> list:
#     return [anime_parser(anime) for anime in animes]

# def get_anime_genre(judul_anime:str):
#     anime = {"judul_anime": {"$regex": judul_anime.capitalize()}}
#     anime_data = (anime_col.find_one(anime))
#     # anime_data_extracted = json.loads(anime_data)
#     return (anime_data['genre_anime'])

# print (get_anime_genre('naruto'))

# example = '{'judul_anime': 'Naruto', 'genre_anime': 'Action'}'

# example1 = example.replace("'", """)

# tes = json.loads(example)
# print (tes['genre_anime'])
