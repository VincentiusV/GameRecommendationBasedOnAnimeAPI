from bs4 import BeautifulSoup
import requests
import json
from tqdm import tqdm

url = "https://myanimelist.net/anime/genre/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

# Membuat class data_gae yang fungsinya untuk membuat setiap game menjadi suatu objek
class data_anime:
    def __init__(self, judul_anime, genre_anime):
        self.judul_anime = judul_anime
        self.genre_anime = genre_anime

genres = ['1/Action', '4/Comedy', '14/Horror', '30/Sports', '2/Adventure', '8/Drama',
            '7/Mystery', '37/Supernatural', '5/Avant_Garde', '10/Fantasy', '22/Romance',
            '41/Suspense', '46/Award_Winning', '26/Girls_Love', '24/Sci-Fi', '28/Boys_Love',
            '47/Gourmet', '36/Slice_of_Life', '9/Ecchi', '49/Erotica', '12/Hentai']

# Membuat sebuah array untuk menampung objek anime
list_anime = []

halaman = 0

for genre in genres:
    # page = requests.get(url+genre)

    for page in range(1, 51):
        halaman += 1
        print ('Scraping Genre : ', genre, ' Total Halaman : ', halaman)
        page = requests.get(url+genre+'?page='+str(page), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        animes = soup.findAll('div', 'title')

        for anime in tqdm(animes):

            # Kolom Judul Anime
            judul_anime = ''.join(anime.find('a', 'link-title').text.split('\n'))

            # Genre Anime
            genre_anime_split = genre.split('/')
            genre_anime = genre_anime_split[1].replace("_", " ")

            # Membuat objek game baru
            anime_baru = data_anime(judul_anime, genre_anime)

            # Menambahkan objek game baru ke dalam array
            list_anime.append(anime_baru)

# Meng-export list_drama ke dalam file berformat json
with open("./database/animelist.json", "w") as write_file:
    json.dump([obj.__dict__ for obj in list_anime], write_file, indent=4)