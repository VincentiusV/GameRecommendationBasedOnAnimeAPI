from bs4 import BeautifulSoup
import requests
import json
from tqdm import tqdm
import string

url = "https://gamesystemrequirements.com/database/"

# Membuat class data_gae yang fungsinya untuk membuat setiap game menjadi suatu objek
class data_game:
    def __init__(self, judul_game, tahun_pembuatan, genre, developer):
        self.judul_game = judul_game
        self.tahun_pembuatan = tahun_pembuatan
        self.genre = genre
        self.developer = developer

# Membuat sebuah array untuk menampung objek game
list_game = []

halaman = 0

for char in list(string.ascii_lowercase)[:26] :
    huruf = char
    page = requests.get(url+str(char))

    for page in range(1, 6):
        halaman += 1
        print ('Scraping Huruf : ', huruf, ' Total Halaman : ', halaman)
        page = requests.get(url+huruf+'/page/'+str(page))
        soup = BeautifulSoup(page.text, 'html.parser')
        games = soup.findAll('a', 'gr_box')

        for game in tqdm(games):

            # Kolom Judul Game
            judul_game = ''.join(game.find('div', 'gr_box_details_title').text.split('\n'))

            # Kolom Game Details
            # game_details = game.find('div', 'gr_box_details_row').text
            game_details = game.find('div', 'gr_box_details_row').text.split("Release date: ")

            try:
                game_details2 = game_details[1].split("Genre: ")    
                game_details3 = game_details2[1].split("Developer: ")
                tahun_pembuatan = game_details2[0]
                genre = game_details3[0]
                developer = game_details3[1]
            except (IndexError):
                continue

            # Membuat objek game baru
            game_baru = data_game(judul_game, tahun_pembuatan, genre, developer)

            # Menambahkan objek game baru ke dalam array
            list_game.append(game_baru)

# Meng-export list_drama ke dalam file berformat json
with open("./database/gamelist.json", "w") as write_file:
    json.dump([obj.__dict__ for obj in list_game], write_file, indent=4)