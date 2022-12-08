from bs4 import BeautifulSoup
import requests

url = "https://gamesystemrequirements.com/game/"

def get_spec(judul_game: str):
    judul_game_final = judul_game.lower().replace(" ", "-")
    page = requests.get(url+judul_game_final)
    if page:
        soup = BeautifulSoup(page.text, 'html.parser')
        specs = soup .findAll('div', 'headline_container')

        for spec in specs:
            spec_game = spec.find('a', 'selected').text.split('.')
        
        spec_game_final = spec_game[1]
        return spec_game_final
    return ("No games found")
