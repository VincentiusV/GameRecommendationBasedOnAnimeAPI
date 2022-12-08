import json

with open('database/gamelist.json') as f:
    data = json.load(f)

for i in data:
    i['genre'] = i['genre'].title()


with open("./database/gamelist.json", "w") as write_file:
    json.dump(data, write_file, indent=4)