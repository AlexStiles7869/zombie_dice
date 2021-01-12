import time
import random
from math import ceil
from helpers import bool_question
from player import Players
from die import Dice

def pluralise(string : str, count : int) -> str:
    new_string = string
    if count != 1:
        new_string = string + "s"
    return new_string

def place_string(place : int) -> str:
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

        self.no_expansion = True if self.args.no_expansion else False

        self.players = Players.initialise_players()

        self.current_player = self.players.starting_player()

        if not self.args.one_loser:
            self.current_player_count = len(self.players)

        self.turn_number = 1
        self.ongoing = True
    
    @staticmethod
    def intro():
        print("-" * 10, "WELCOME TO ZOMBIE DICE", "-" * 10)
        no_rules = bool_question("Have you played zombie dice before? (yes or no) ", ["yes", "no"])
        if not no_rules:
            print("ZOMBIE DICE RULES:")
            print("Rules will be added here.")

    def turn(self):
        print("-" * 20)
        print(f"Round {ceil(self.turn_number / self.current_player_count)} | It is {self.current_player.name}'s turn.")
        print(f"Current Brains | {self.current_player.collected_brains}")
        print("-" * 20)
        time.sleep(1)

        can_play = True
        dice = Dice()
        selected_dice = []

        while can_play:
            # Calculate and get the number of new dice required to be drawn from the cup
            number_of_new_dice = 3 - len(selected_dice)
            selected_dice += dice.get_random_dice(number_of_new_dice)

            # For each of the dice, roll them, and remove them if they didn't run away (there action has been completed)
            for i in range(len(selected_dice) - 1, -1, -1):
                die_played = self.roll_die(selected_dice[i])
                if die_played:
                    selected_dice.remove(selected_dice[i])
            
            # If the player has not won the game and lost their turn provide the option to continue
            if not self.win_check() and not self.lose_check():
                print("-" * 10)
                can_play = bool_question("Roll again? ", ["yes", "no"])
                if can_play:
                    print("-" * 10)
                
                # Add the brains they collected during their turn to their stored total
                if not can_play:
                    self.current_player.collected_brains += self.current_player.turn_brains
            else:
                # If the player has meet the win condition (>= 13 brains) and did not lose the round that got them the last required brains
                if self.win_check() and not self.lose_check():
                    self.won()
                
                can_play = False

        # Change the player
        self.next_turn()

    def next_turn(self):
        # Reset the current players turn based stats before going to next player
        self.current_player.turn_brains = 0
        self.current_player.collected_shotguns = 0

        self.players.next_player()
        self.current_player = self.players.curr_player
        self.turn_number += 1

    def win_check(self) -> bool:
        return self.current_player.collected_brains + self.current_player.turn_brains >= 13
    
    def won(self):
        print(f"Congratulations {self.current_player.name}! You have won.")

        self.ongoing = False

    def lose_check(self) -> bool:
        return self.current_player.collected_shotguns >= 3

    def roll_die(self, die) -> int:
        die_roll = die.roll()
        die_face = die_roll.face_type
        die_face_count = die_roll.count

        if die_face == "SHOTGUN":
            self.current_player.collected_shotguns += die_face_count
            shotgun_count = self.current_player.collected_shotguns
            print(f"{die.die_type}: You collected {die_face_count} {pluralise('shot', shotgun_count)}, you now have {shotgun_count} {pluralise('shot', shotgun_count)}.")
            time.sleep(1)
        elif die_face == "BRAIN":
            self.current_player.turn_brains += die_face_count
            brain_count = self.current_player.turn_brains
            print(f"{die.die_type}: You collected {die_face_count} {pluralise('brain', brain_count)}, you would now have {self.current_player.collected_brains + brain_count} {pluralise('brain', brain_count)} if you banked.")
            time.sleep(1)
        elif die_face == "RUN":
            print(f"{die.die_type}: The person you were chasing ran away!")
            time.sleep(1)
        
        return True if die_face != "RUN" else False