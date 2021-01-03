from player import Players

players = Players()
players.add_player("Alex", 18)
players.add_player("Edward", 19)
players.add_player("Chris", 19)
players.add_player("Beowulf", 18)
players.add_player("Kieran", 19)
# print(players.curr_player.name)
# players.next_player()
# print(players.curr_player.name)

for i in range(len(players) * 2):
    if i == 2:
        try:
            players.remove_player("Chris")
        except ValueError as e:
            print(str(e))
    the_player = players.curr_player
    print(f"{i}: {the_player.name} -> {the_player.next_player.name if the_player.next_player is not None else ''}")
    players.next_player()

print(players.starting_player().name)