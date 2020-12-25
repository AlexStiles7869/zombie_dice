class Player:

    id_counter = 0
    
    def __init__(self, name : str, age : int):
        self.id = self.id_counter
        self.id_counter += 1

        self.name = name
        self.age = age

        self.collected_brains = 0
        self.collected_shotguns = 0

    @staticmethod
    def initialise_players():
        entering = True
        players = []
        while entering:
            player_name = Player.validate_name("What is the player's name? ")
            player_age = Player.validate_age("What is the player's age? ")
            player_instance = Player(player_name, player_age)
            players.append(player_instance)
            if len(players) > 1:
                entering = False
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