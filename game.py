import random
from player import Player
from die import Die

class Game:
    def __init__(self):
        self.players = Player.initialise_players()
        self.current_player = self.starting_player()
        self.turn_number = 0 
        self.ongoing = True
    
    def starting_player(self):
        """ Determines the starting player, who is the youngest. """
        # shuffled_players = self.players.copy()
        # random.shuffle(shuffled_players)
        starting_player = None
        if (filter(lambda player: player.age == self.players[0].age, self.players[1:])):
            starting_player = self.players[random.randint(0, len(self.players) - 1)]
        else:
            starting_player = min(self.players, key=lambda player: player.age)
        return starting_player
    
    def check_for_win(self):
        return self.current_player.collected_brains < 13

    def won(self):
        self.ongoing = False

    def check_for_turn_loss(self):
        return self.current_player.collected_shotguns < 3

    def loss(self):
        pass

    def next_turn(self):
        self.turn_number += 1
        self.current_player = self.next_player()

    def turn(self):
        print("You pick 3 random dice out of the cup and get:\n")
        random_dice = []
        print(self.check_for_turn_loss(), self.check_for_win())
        while self.check_for_turn_loss() and self.check_for_win():
            # While you haven't gotten 3 shotguns and haven't won
            for i in range(3 - len(random_dice)):
                random_die = Die(random.choice(Die.ALLOWED_TYPES))
                random_dice.append(random_die)
                print(f"A {random_die.die_type.lower()} die.\n")
            self.current_player.collected_shotguns += 1
            self.current_player.collected_brains += 1
            print(self.current_player.collected_brains, self.current_player.collected_shotguns)
        if not self.check_for_win():
            # This round allowed you to win
            self.won()
        else:
            self.next_turn()
            # You finished the round
    
    def next_player(self):
        return self.players[self.turn_number % len(self.players)]