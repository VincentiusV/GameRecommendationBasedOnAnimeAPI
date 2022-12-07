from database import anime_col
import json

def anime_parser(anime) -> dict:
    return {
        "id": str(anime["_id"]),
        "judul_anime": anime["judul_anime"],
        "genre_anime": anime["genre_anime"]
    }

def anime_serializer(animes) -> list:
    return [anime_parser(anime) for anime in animes]

def get_anime_genre(judul_anime:str):
    anime = {"judul_anime": {"$regex": judul_anime.capitalize()}}
    anime_data = (anime_col.find_one(anime))
    # anime_data_extracted = json.loads(anime_data)
    return (anime_data['genre_anime'])

print (get_anime_genre('naruto'))

# example = '{'judul_anime': 'Naruto', 'genre_anime': 'Action'}'

# example1 = example.replace("'", """)

# tes = json.loads(example)
# print (tes['genre_anime'])
