class Die:

    ALLOWED_TYPES = ["GREEN", "ORANGE", "RED"]

    def __init__(self, die_type : str):
        self.die_type = die_type

        self.set_die_attributes()

    def set_die_attributes(self):
        """ Set the die attributes such as brain, run, and shotgun counts. """
        if self.die_type in self.ALLOWED_TYPES:
            if self.die_type == self.ALLOWED_TYPES[0]:
                self.brains = 3
                self.runs = 2
                self.shotguns = {"CNT": 1, "DMG": 1}
            elif self.die_type == self.ALLOWED_TYPES[1]:
                self.brains = 2
                self.runs = 2
                self.shotguns = {"CNT": 2, "DMG": 1}
            elif self.die_type == self.ALLOWED_TYPES[2]:
                self.brains = 1
                self.runs = 2
                self.shotguns = {"CNT": 3, "DMG": 1}
        else:
            raise ValueError(f"The die type {self.die_type} is not in {self.ALLOWED_TYPES} and is therefore not valid")
    