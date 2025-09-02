players =  [
    {'id' : 101, 'name' : 'Player1'},
    {'id' : 102, 'name' : 'Player2'}
]

print(players)

player = {}
# player = dict()
player['id'] = 103
player['name'] = 'vinayak'
print(players)

for player in players:
    if player['id'] == 103:
        print(player)


players_dict = {101:players[0], 102:players[1],103:players[2]}

print(players_dict[103])


