import random
from helpers import bool_question

class Player:

    id_counter = 0
    
    def __init__(self, name : str, age : int):
        self.id = self.id_counter
        self.id_counter += 1

        self.next_player = None

        self.name = name
        self.age = age

        self.turn_brains = 0

        self.collected_brains = 0
        self.collected_shotguns = 0
        
class Players:
    def __init__(self):
        self.end = None
        self.curr_player = None
        self.length = 0
    
    @staticmethod
    def initialise_players():
        entering = True
        players = Players()
        print("-" * 10, "ENTER PLAYER DETAILS", "-" * 10)
        while entering:
            player_name = Players.validate_name("What is the player's name? ")
            player_age = Players.validate_age("What is the player's age? ")
            players.add_player(player_name, player_age)
            if len(players) > 1:
                entering = bool_question("Would you like to enter another player? (yes or no) ", ["yes", "no"])
        return players

    @staticmethod
    def validate_name(question : str): 
        valid = False
        while not valid:
            name = input(question)
            if name and name.isalpha():
                valid = True
            else:
                print("Please enter a name containing only letters.")
        return name

    @staticmethod
    def validate_age(question : str):
        valid = False
        while not valid:
            try:
                age = int(input(question))
                if age < 0 and age > 150:
                    raise ValueError
                else:
                    valid = True
            except ValueError:
                print("Please enter an age equal or large than 0 and less than 150.")
            except TypeError:
                print("Please enter a whole number.")

        return age

    def add_player(self, name : str, age : int):
        new_player = Player(name, age)
        if self.end is None:
            self.end = new_player
        else:
            new_player.next_player = self.curr_player
            self.end.next_player = new_player

        self.curr_player = new_player
        self.length += 1

    def remove_player(self, player_name):
        current = self.curr_player
        i = 0
        while i < len(self):
            if current.next_player.name == player_name:
                break
            current = current.next_player
            i += 1
        if current.next_player.name == player_name:
            current.next_player = current.next_player.next_player
            self.length -= 1
        else:
            raise ValueError(f"The player '{player_name}' doesn't exist")

    def starting_player(self):
        lowest_aged_player = None
        same_aged_players = []
        current = self.curr_player
        i = 0
        while i < len(self):
            if lowest_aged_player is None or current.age < lowest_aged_player.age:
                lowest_aged_player = current
            elif current.age == lowest_aged_player.age:
                same_aged_players.append(current)

            current = current.next_player
            i += 1

        if len(same_aged_players):
            same_aged_players.append(lowest_aged_player)
            lowest_aged_player = random.choice(same_aged_players)

        self.curr_player = lowest_aged_player

        return lowest_aged_player

    def next_player(self):
        self.curr_player = self.curr_player.next_player
    
    def __len__(self):
        return self.length