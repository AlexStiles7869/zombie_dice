import random

class DieFace:

    def __init__(self, face_type, count=1):
        self.face_type = face_type
        self.count = count

class Die:

    def __init__(self, die_type : str):
        self.die_type = die_type
        self.faces = self.set_die_attributes()
        
    def set_die_attributes(self):
        """ Set the die attributes such as brain, run, and shotgun counts. """
        faces = []

        if self.die_type == "GREEN":
            faces = [DieFace("BRAIN"), 
                     DieFace("BRAIN"), 
                     DieFace("BRAIN"), 
                     DieFace("RUN"), 
                     DieFace("RUN"), 
                     DieFace("SHOTGUN")
            ]
        elif self.die_type == "ORANGE":
            faces = [DieFace("BRAIN"), 
                     DieFace("BRAIN"), 
                     DieFace("RUN"), 
                     DieFace("RUN"), 
                     DieFace("SHOTGUN"), 
                     DieFace("SHOTGUN")
            ]
        elif self.die_type == "RED":
            faces = [DieFace("BRAIN"), 
                     DieFace("RUN"), 
                     DieFace("RUN"), 
                     DieFace("SHOTGUN"), 
                     DieFace("SHOTGUN"), 
                     DieFace("SHOTGUN")
            ]
        else:
            raise ValueError(f"The provided die_type '{self.die_type}' is invalid.")
        
        return faces

    def roll(self):
        return random.choice(self.faces)

class Dice:

    def __init__(self):
        # It's not very nice how I'm creating the lists here. Will cleanup later.
        self.dice = self.set_default()

    def set_default(self):
        return [
            Die("GREEN"),
            Die("GREEN"),
            Die("GREEN"),
            Die("GREEN"),
            Die("GREEN"),
            Die("GREEN"),
            Die("ORANGE"),
            Die("ORANGE"),
            Die("ORANGE"),
            Die("ORANGE"),
            Die("RED"),
            Die("RED"),
            Die("RED")
        ]

    def get_random_dice(self, num):
        random_dice = []
        if num > len(self.dice):
            self.dice = self.set_default()
        for i in range(num):
            selected_die = random.choice(self.dice)
            self.dice.remove(selected_die)
            random_dice.append(selected_die)
            # die_index = random.randint(0, len(self.dice) - 1)
            # random_dice.append(self.dice.pop(die_index))
        return random_dice