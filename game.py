import random
from player import Players
from die import Dice

def question(question : str, valid_responses : list) -> bool:
    response = None
    answer = input(question)
    while response is None:
        try:
            if answer in valid_responses:
                if answer == valid_responses[0]:
                    response = True
                else:
                    response = False
            else:
                raise ValueError(f"Your response '{answer}' isn't one of the valid options")
        except ValueError as e:
            print(str(e))
            answer = input(question)
    return response

def place_string(place : int) :
    if place == 1:
        place_string = "1st"
    elif place == 2:
        place_string = "2nd"
    elif place == 3:
        place_string = "3rd"
    else:
        place_string = f"{place}th"

    return place_string

class Game:
    def __init__(self, args):

        self.args = args

        self.no_expansion = self.args.ne

        # self.players = Players.initialise_players()

        self.players = Players()
        self.players.add_player("Alex", 19)
        self.players.add_player("Edward", 19)

        self.current_player = self.players.starting_player()

        if not self.args.ol:
            self.current_player_count = len(self.players)

        self.turn_number = 1
        self.ongoing = True
    
    @staticmethod
    def print_rules():
        print("ZOMBIE DICE RULES:")
        print("Rules will be added here.")

    # def starting_player(self):
    #     """ Determines the starting player by who is the youngest. """
    #     starting_player = None
    #     if (filter(lambda player: player.age == self.players[0].age, self.players[1:])):
    #         starting_player = self.players[random.randint(0, len(self.players) - 1)]
    #     else:
    #         starting_player = min(self.players, key=lambda player: player.age)
    #     return starting_player

    def turn(self):
        print(f"It is {self.current_player.name}'s turn.")
        self.current_player.collected_shotguns = 0
        continuing = True
        dice = Dice()
        while not self.check_for_turn_loss() and not self.check_for_win() and continuing:
            selected_dice = dice.get_random_dice(3)
            for die in selected_dice:
                die_roll = die.roll()
                die_face = die_roll.face_type
                die_face_count = die_roll.count
                if die_face == "SHOTGUN":
                    self.current_player.collected_shotguns += die_face_count
                    print(f"{die.die_type}: You collected {die_face_count} shots, you now have {self.current_player.collected_shotguns} shots.")
                    if self.check_for_turn_loss():
                        self.turn_loss()
                        break
                elif die_face == "BRAIN":
                    self.current_player.collected_brains += die_face_count
                    print(f"{die.die_type}: You collected {die_face_count} brains, you now have {self.current_player.collected_brains} brains.")
                    if self.check_for_win():
                        self.won()
                        break
                elif die_face == "RUN":
                    print(f"{die.die_type}: The person you were chasing ran away!")
            for die in dice.dice:
                print(die.die_type, end=" ")
            print()
            if not self.check_for_turn_loss() and not self.check_for_win():
                continuing = question("Would you like to continue? (yes or no) ", ["yes", "no"])
            else:
                continuing = False
        else:
            self.next_turn()

    def next_turn(self):
        self.turn_number += 1
        self.next_player()
        self.current_player = self.players.curr_player

    def next_player(self):
        # return self.players[self.turn_number % self.current_player_count]
        self.players.next_player()

    def check_for_turn_loss(self):
        return self.current_player.collected_shotguns >= 3

    def turn_loss(self):
        print(f"Your turn is over as you have {self.current_player.collected_shotguns} shots.")
        # self.next_turn()

    def check_for_win(self):
        return self.current_player.collected_brains >= 13

    def won(self):
        """ This message is shown to the player who first gets 13 brains """
        
        # if self.args.ol or self.current_player_count == len(self.players):
        #     """ This is the first person to win the game """
        #     print(f"Congradulations {self.current_player}. You have won!")
        # else:
        #     self.current_player_count -= 1
        #     place = self.players - self.current_player_count
        #     print(f"Good job. You came {place_string(place)}")

        if not self.args.ol:
            self.ongoing = False

    def loss(self):
        """ If there can be more than one loser (self.args.ol = False), this method is called when there is only one player remaining and they have therefore lost the game """
        pass