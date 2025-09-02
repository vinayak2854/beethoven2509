import json
players =  [
    {'id' : 101, 'name' : 'Player1'},
    {'id' : 102, 'name' : 'Player2'}
]

print(players)


with open('players.json', 'w') as file:
    json.dump(players, file)


with open('players.json', 'r') as reader:
    players_from_json = json.load(reader)
    print(players_from_json)